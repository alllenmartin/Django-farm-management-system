# Generated by Django 3.0.7 on 2020-06-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200629_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='farm',
            name='other_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
