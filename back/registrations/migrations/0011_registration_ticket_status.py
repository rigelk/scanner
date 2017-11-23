# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 10:27
from __future__ import unicode_literals

from django.db import migrations, models


def initialize_ticket_status_field(apps, schema_editor):
    Registration = apps.get_model('registrations', 'Registration')

    Registration.objects.filter(ticket_sent=True).update(ticket_status='S')
    Registration.objects.filter(ticket_sent=False).update(ticket_status='N')


def revert_back_on_ticket_sent(apps, schema_editor):
    Registration = apps.get_model('registrations', 'Registration')

    Registration.objects.filter(ticket_status='S').update(ticket_sent=True)
    Registration.objects.exclude(ticket_status='S').update(ticket_sent=False)


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0010_auto_20171122_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='ticket_status',
            field=models.CharField(choices=[('N', 'Ticket non envoyé'), ('M', "Ticket modifié depuis l'envoi"), ('S', 'Ticket à jour envoyé')], default='N', max_length=1, verbose_name='Statut du ticket'),
        ),
        migrations.RunPython(
            code=initialize_ticket_status_field,
            reverse_code=revert_back_on_ticket_sent,
        ),
        migrations.RemoveField(
            model_name='registration',
            name='ticket_sent'
        )
    ]