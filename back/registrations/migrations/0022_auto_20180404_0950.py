# Generated by Django 2.0.4 on 2018-04-04 09:50

from django.db import migrations, models
import registrations.models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0021_auto_20180403_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketevent',
            name='ticket_template',
            field=models.FileField(blank=True, upload_to=registrations.models.TicketEvent.get_template_filename, verbose_name='Template du ticket'),
        ),
    ]