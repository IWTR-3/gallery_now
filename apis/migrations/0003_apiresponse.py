# Generated by Django 3.2.18 on 2023-05-18 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20230518_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml', models.TextField()),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.api')),
            ],
        ),
    ]
