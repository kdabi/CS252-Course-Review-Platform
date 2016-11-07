# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20161030_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_credit',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='summary',
            field=models.CharField(default='Summary', max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_details',
            field=models.TextField(default='Not yet decided'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_preReq',
            field=models.CharField(default='None', max_length=1000),
        ),
    ]
