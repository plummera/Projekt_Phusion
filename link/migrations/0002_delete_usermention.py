# Generated by Django 2.0.2 on 2018-05-05 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserMention',
        ),
    ]