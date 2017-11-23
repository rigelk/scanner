# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0011_registration_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='person',
            field=models.CharField(default='inconnu⋅e', max_length=255, verbose_name='Le nom de la personne ayant scanné'),
            preserve_default=False,
        ),
    ]