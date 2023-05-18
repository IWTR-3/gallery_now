from django.db import models
from django.contrib.auth import get_user_model
from apis.models import *
from django.conf import settings
from taggit.managers import TaggableManager  # 👈 for taggit
from taggit.models import (
    TagBase,
    TaggedItemBase
)


class Gallery(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    CLOSED_DAYS_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    closed_days = models.CharField(max_length=10, choices=CLOSED_DAYS_CHOICES)
    phone_number = models.CharField(max_length=30)


class Artist(models.Model):
    name_ko = models.CharField(max_length=30)
    name_en = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    COUNTRIES = [
        ('KOR', 'South Korea'),
        ('USA', 'United States'),
        ('JPN', 'Japan'),
        ('CHN', 'China'),
        # Add more countries as needed
    ]
    nationality = models.CharField(max_length=3, choices=COUNTRIES)


class Exhibition(models.Model):
    REQUIRED_FIELDS = ['title', 'period', 'time', 'charge',
                       'grade']  # 'thumbnail'

    def img_path(instance):
        return f'posts/thumbnails/'

    title = models.CharField(max_length=100)
    period = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    address = models.CharField(max_length=100, blank=True)
    time = models.CharField(max_length=100, blank=True)
    charge = models.CharField(max_length=100, blank=True)
    grade = models.CharField(max_length=100, blank=True)
    venue = models.TextField(max_length=100, blank=True)

    thumbnail = models.ImageField(upload_to=img_path, blank=True)
    item = models.ForeignKey(
        Item, on_delete=models.SET_DEFAULT, default=1)

    tags = TaggableManager()


"""
for item in Item.objects.all():
    data = {
        'title': item.title[:100],
        'period': item.period[:100],
        'description': item.description,
        'address': ""[:100],
        'time': item.time[:100],
        'charge': item.charge[:100],
        'grade': item.grade[:100],
        'venue': item.venue[:100],
        'thumbnail': item.thumbnail,
        'item': item,
        'tags': item.title + item.description,
    }
    form = ExhibitionForm(data=data)
    if form.is_valid():
        form.save() 
"""


class Review(models.Model):
    exhibition = models.ForeignKey(
        Exhibition, on_delete=models.SET_DEFAULT, default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_DEFAULT, default=1)
    content = models.CharField(max_length=255)


class Theme(models.Model):
    def img_path(instance):
        return f'themes/thumbnails/'
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    thumbnails = models.ImageField(upload_to=img_path, blank=True)
    exhibitions = models.ManyToManyField(Exhibition, related_name='themes')

    # on_delete=models.SET_NULL, null=True
