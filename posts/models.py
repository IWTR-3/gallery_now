from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

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
    title = models.CharField(max_length=30)
    fees = models.IntegerField(null=True)
    address = models.CharField(max_length=30)
    gallery = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True)
    begin = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    image = models.ImageField(null=True)
    artists = models.ManyToManyField(Artist, related_name='exhibitions')

class Review(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.SET_NULL, null=True)
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


    # on_delete=models.SET_NULL, null=True