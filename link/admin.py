# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Psychic, Update, UserMention, TweetDefault, Tweet, Intel

# Register your models here.
class IntelAdmin(admin.ModelAdmin):
    fields = ['category', 'metric']

class PsychicAdmin(admin.ModelAdmin):
    fields = ['name', 'host', 'port', 'profession', 'connect_attempt', 'level']

class UpdateAdmin(admin.ModelAdmin):
    fields = ['name', 'owner', 'event', 'post_date']

class UserMentionAdmin(admin.ModelAdmin):
    fields = ['ident', 'name', 'screen_name']

class TweetAdmin(admin.ModelAdmin):
    fields = ['created_at', 'description', 'favorites_count', 'followers_count', 'friends_count', 'ident', 'lang', 'location', 'name', 'profile_background_color', 'profile_background_image_url', 'profile_banner_url', 'profile_image_url', 'profile_link_color', 'profile_sidebar_fill_color', 'profile_text_color', 'protected', 'status_count', 'time_zone', 'url', 'utc_offset']

class TweetDefaultAdmin(admin.ModelAdmin):
    fields = ['created_at', 'hashtags', 'ident', 'id_str', 'lang', 'source', 'text', 'urls', 'user']

admin.site.register(UserMention, UserMentionAdmin)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(TweetDefault, TweetDefaultAdmin)
admin.site.register(Psychic, PsychicAdmin)
admin.site.register(Update, UpdateAdmin)
admin.site.register(Intel, IntelAdmin)
