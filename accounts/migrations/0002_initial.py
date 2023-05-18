# Generated by Django 3.2.18 on 2023-05-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_exhibitions',
            field=models.ManyToManyField(related_name='like_users', to='posts.Exhibition'),
        ),
        migrations.AddField(
            model_name='user',
            name='visited_exhibitions',
            field=models.ManyToManyField(related_name='visited_users', to='posts.Exhibition'),
        ),
    ]
