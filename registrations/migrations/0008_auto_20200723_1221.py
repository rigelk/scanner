# Generated by Django 2.2.14 on 2020-07-23 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("registrations", "0007_scanpoint"),
    ]

    operations = [
        migrations.AddField(
            model_name="scanneraction",
            name="point",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="actions",
                to="registrations.ScanPoint",
            ),
        ),
        migrations.AddField(
            model_name="scanpoint",
            name="count",
            field=models.BooleanField(
                default=False, verbose_name="Afficher le compteur"
            ),
        ),
        migrations.CreateModel(
            name="ScanSeq",
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
                    "created",
                    models.DateTimeField(
                        auto_created=True, verbose_name="Début du créneau"
                    ),
                ),
                (
                    "point",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seqs",
                        to="registrations.ScanPoint",
                    ),
                ),
            ],
        ),
    ]
