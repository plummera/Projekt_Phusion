# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.forms.utils import flatatt
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _

from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
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

class Analysis(models.Model):
    category = models.CharField(max_length=120)
    metric = models.FloatField(default=0)

    def __str__(self):
        return self.category

class Intel(models.Model):
    category = models.CharField(max_length=120)
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
    time_zone = models.CharField(max_length=40, blank=True)
    url = models.CharField(max_length=200, blank=True)
    utc_offset = models.IntegerField(blank=True, default=0)
    text = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.name

class Update(models.Model):
    name = models.CharField(max_length=40)
    owner = models.CharField(max_length=40, blank=True)
    event = models.CharField(blank=True, max_length=5000)
    post_date = models.DateField("Date")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return self.name

class FaceBookUser(models.Model):
    name = models.CharField(max_length=40, blank=False)
    id = models.BigIntegerField(blank=True, primary_key=True)

    def __str__(self):
        return self.name

class Cryptocurrency(models.Model):
    data = models.TextField()

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user
