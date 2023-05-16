from django.db import models
from django.contrib.auth import get_user_model
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
    FIELDS = ['title', 'period', 'time', 'charge',
              'grade', ]  # 'thumbnail'

    def img_path(instance):
        return f'posts/thumbnails/{instance.pk}.jpg'

    title = models.CharField(max_length=100)
    period = models.CharField(max_length=100, null=True)
    time = models.CharField(max_length=100, null=True)
    charge = models.CharField(max_length=100, null=True)
    grade = models.CharField(max_length=100, null=True)
    # referenceIdentifier = models.URLField(default="")
    thumbnail = models.ImageField(
        '대표이미지', upload_to='img_path', blank=True)
    tags = TaggableManager()


class Review(models.Model):
    exhibition = models.ForeignKey(
        Exhibition, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=255)
    STAR_CHOICES = (
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars'),
    )
    star = models.CharField(max_length=1, choices=STAR_CHOICES)


class Theme(models.Model):
    title = models.CharField(max_length=30)
    exhibitions = models.ManyToManyField(Exhibition, related_name='themes')

    # on_delete=models.SET_NULL, null=True
