# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-05 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0002_auto_20171205_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='ScreenName',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='tweet',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='tweet',
            name='favorites_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='followers_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='friends_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='ident',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='lang',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='tweet',
            name='location',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name='tweet',
            name='name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='tweet',
            name='profile_background_color',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='tweet',
            name='profile_background_image_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='tweet',
            name='profile_banner_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='tweet',
            name='profile_image_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='tweet',
            name='profile_link_color',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='tweet',
            name='profile_sidebar_fill_color',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='tweet',
            name='profile_text_color',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='tweet',
            name='protected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tweet',
            name='status_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='time_zone',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='tweet',
            name='url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='tweet',
            name='utc_offset',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
