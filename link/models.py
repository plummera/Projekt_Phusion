# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers

# Create your models here.
class Profile(models.Model):
    category = models.CharField(max_length=24)
    name = models.CharField(max_length=60)
    ident = models.IntegerField(default=0)
    result = models.FloatField(default=0)

class Psychic(models.Model):
    name = models.CharField(max_length=30)
    CLASSES = (
        ("p(S)ychic", 'S'),
        ("(W)arrior", 'W'),
        ("(T)hief", 'T'),
        ("(M)age", 'M'),
        ("(C)leric", 'C'),
        ("Mon(K)", 'K'),
        ("(P)aladin", 'P'),
        ("(D)ruid", 'D'),
        ("(Tr)raveller", 'Traveller'),
        ("Jack of Clubs", 'Joker'),
    )
    ATTEMPT_RESULT = (
        ("HIT", 'HIT'),
        ("MISS", 'MISS'),
    )
    host = models.CharField(max_length=50, default='theland.notroot.com')
    port = models.IntegerField(default=4000)
    level = models.CharField(default="Unknown", max_length=20)
    profession = models.CharField(max_length=15, choices=CLASSES)
    connect_attempt = models.CharField(max_length=15, choices=ATTEMPT_RESULT, default='MISS')

    def __str__(self):
        return self.name

class Intel(models.Model):
    category = models.CharField(max_length=40)
    metric = models.FloatField(default=0)

    def __str__(self):
        return self.category

class Tweet(models.Model):
    created_at = models.DateField("Created at:")
    description = models.CharField(max_length=500, blank=True)
    favorites_count = models.IntegerField(blank=True, default=0)
    followers_count = models.IntegerField(blank=True, default=0)
    friends_count = models.IntegerField(blank=True, default=0)
    ident = models.IntegerField(blank=False, default=000000000)
    lang = models.CharField(max_length=2, blank=True)
    location = models.CharField(max_length=4, blank=True)
    name = models.CharField(max_length=25, blank=True)
    profile_background_color = models.CharField(max_length=10, blank=True)
    profile_background_image_url = models.CharField(max_length=200, blank=True)
    profile_banner_url = models.CharField(max_length=200, blank=True)
    profile_image_url = models.CharField(max_length=200, blank=True)
    profile_link_color =models.CharField(max_length=10, blank=True)
    profile_sidebar_fill_color = models.CharField(max_length=10, blank=True)
    profile_text_color = models.CharField(max_length=10, blank=True)
    protected = models.BooleanField(default=False)
    ScreenName = models.CharField(max_length=25, blank=True)
    status_count = models.IntegerField(blank=True, default=0)
    time_zone = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=200, blank=True)
    utc_offset = models.IntegerField(blank=True, default=0)
    text = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.name

class Update(models.Model):
    name = models.CharField(max_length=40)
    owner = models.CharField(max_length=60, blank=True)
    event = models.CharField(blank=True, max_length=200)
    post_date = models.DateField("Date")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['post_date']

class UserMention(models.Model):
    ident = models.IntegerField(blank=False, default=00000000)
    name = models.CharField(max_length=50, blank=True)
    screen_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class FaceBookUser(models.Model):
    name = models.CharField(max_length=40, blank=False)
    id = models.BigIntegerField(blank=True, primary_key=True)

    def __str__(self):
        return self.name
