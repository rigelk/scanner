# Generated by Django 2.2.14 on 2020-07-22 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("registrations", "0006_auto_20190822_0820"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScanPoint",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Point de scan"),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="scan_points",
                        to="registrations.TicketEvent",
                    ),
                ),
            ],
        ),
    ]
