from django.db import models

# Create your models here.


class Api(models.Model):
    title = models.TextField()
    server = models.TextField()
    path = models.TextField()
    param_keys = models.TextField()
    field_keys = models.TextField()


class Item(models.Model):
    def img_path(instance):
        return f'posts/thumbnails/'

    api = models.IntegerField()
    thumbnail = models.ImageField(upload_to=img_path, blank=True)

    abstractDesc = models.TextField(blank=True)
    affiliation = models.TextField(blank=True)
    alternativeTitle = models.TextField(blank=True)
    charge = models.TextField(blank=True)
    collectionDb = models.TextField(blank=True)
    contributor = models.TextField(blank=True)
    copyrightOthers = models.TextField(blank=True)
    coverage = models.TextField(blank=True)
    createdDate = models.TextField(blank=True)
    creator = models.TextField(blank=True)
    description = models.TextField(blank=True)
    digitalizedDate = models.TextField(blank=True)
    extent = models.TextField(blank=True)
    format = models.TextField(blank=True)
    grade = models.TextField(blank=True)
    identifier = models.TextField(blank=True)
    insertDate = models.TextField(blank=True)
    issuedDate = models.TextField(blank=True)
    language = models.TextField(blank=True)
    medium = models.TextField(blank=True)
    period = models.TextField(blank=True)
    person = models.TextField(blank=True)
    publisher = models.TextField(blank=True)
    reference = models.TextField(blank=True)
    referenceIdentifier = models.TextField(blank=True)
    regDate = models.TextField(blank=True)
    relation = models.TextField(blank=True)
    rights = models.TextField(blank=True)
    source = models.TextField(blank=True)
    spatial = models.TextField(blank=True)
    subjectCategory = models.TextField(blank=True)
    subjectKeyword = models.TextField(blank=True)
    subDescription = models.TextField(blank=True)
    tableOfContents = models.TextField(blank=True)
    temporal = models.TextField(blank=True)
    time = models.TextField(blank=True)
    title = models.TextField(blank=True)
    type = models.TextField(blank=True)
    uci = models.TextField(blank=True)
    url = models.TextField(blank=True)
    venue = models.TextField(blank=True)
    temporalCoverage = models.TextField(blank=True)
    sourceTitle = models.TextField(blank=True)
    eventPeriod = models.TextField(blank=True)


"""
strings = 
strings = list(strings.split('\n'))
strings = '_'.join(strings)
strings
"""
# thumbnail < thumbnail
# artist
# title < title
# period < period
# time < time
# venue < venue
# address
# closed_date
# charge
# contact < reference
# url < url
