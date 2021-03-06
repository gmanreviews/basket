# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=999)),
                ('pdf_location', models.CharField(max_length=200)),
                ('audio_location', models.CharField(max_length=200)),
                ('paperback', models.BooleanField(default=0)),
                ('pdf', models.BooleanField(default=0)),
                ('audio', models.BooleanField(default=0)),
            ],
        ),
    ]
