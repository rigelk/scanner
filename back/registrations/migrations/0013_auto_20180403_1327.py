# Generated by Django 2.0.4 on 2018-04-03 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0012_event_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='person',
            field=models.CharField(max_length=255, verbose_name='Personne ayant scanné'),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events', to='registrations.Registration'),
        ),
    ]
