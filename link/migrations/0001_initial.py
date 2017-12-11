# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-05 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Psychic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('host', models.CharField(default='theland.notroot.com', max_length=50)),
                ('port', models.IntegerField(default=4000)),
                ('level', models.CharField(default='Unknown', max_length=20)),
                ('profession', models.CharField(choices=[('p(S)ychic', 'S'), ('(W)arrior', 'W'), ('(T)hief', 'T'), ('(M)age', 'M'), ('(C)leric', 'C'), ('Mon(K)', 'K'), ('(P)aladin', 'P'), ('(D)ruid', 'D'), ('(Tr)raveller', 'Traveller'), ('Jack of Clubs', 'Joker')], max_length=15)),
                ('connect_attempt', models.CharField(choices=[('HIT', 'HIT'), ('MISS', 'MISS')], default='MISS', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Created at:')),
                ('description', models.CharField(blank=True, max_length=500)),
                ('favorites_count', models.IntegerField(blank=True, default=0)),
                ('followers_count', models.IntegerField(blank=True, default=0)),
                ('friends_count', models.IntegerField(blank=True, default=0)),
                ('ident', models.IntegerField(default=0)),
                ('lang', models.CharField(blank=True, max_length=2)),
                ('location', models.CharField(blank=True, max_length=4)),
                ('name', models.CharField(blank=True, max_length=25)),
                ('profile_background_color', models.CharField(blank=True, max_length=10)),
                ('profile_background_image_url', models.CharField(blank=True, max_length=200)),
                ('profile_banner_url', models.CharField(blank=True, max_length=200)),
                ('profile_image_url', models.CharField(blank=True, max_length=200)),
                ('profile_link_color', models.CharField(blank=True, max_length=10)),
                ('profile_sidebar_fill_color', models.CharField(blank=True, max_length=10)),
                ('profile_text_color', models.CharField(blank=True, max_length=10)),
                ('protected', models.BooleanField(default=False)),
                ('ScreenName', models.CharField(blank=True, max_length=25)),
                ('status_count', models.IntegerField(blank=True, default=0)),
                ('time_zone', models.CharField(blank=True, max_length=50)),
                ('url', models.CharField(blank=True, max_length=200)),
                ('utc_offset', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TweetDefault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Created at:')),
                ('hashtags', models.CharField(blank=True, max_length=40)),
                ('ident', models.IntegerField(default=0)),
                ('id_str', models.IntegerField(default=0)),
                ('lang', models.CharField(default='en', max_length=2)),
                ('source', models.CharField(blank=True, max_length=500)),
                ('text', models.CharField(blank=True, max_length=900)),
                ('urls', models.CharField(blank=True, max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='link.Tweet')),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('owner', models.CharField(blank=True, max_length=60)),
                ('event', models.CharField(blank=True, max_length=200)),
                ('post_date', models.DateField(verbose_name='Date')),
            ],
            options={
                'ordering': ['post_date'],
            },
        ),
        migrations.CreateModel(
            name='UserMention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.IntegerField(default=0)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('screen_name', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
