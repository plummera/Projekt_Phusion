# Generated by Django 2.1.3 on 2019-02-05 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=120)),
                ('metric', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='intel',
            name='category',
            field=models.CharField(max_length=120),
        ),
    ]
