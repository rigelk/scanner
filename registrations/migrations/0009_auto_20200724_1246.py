# Generated by Django 2.2.14 on 2020-07-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registrations", "0008_auto_20200723_1221"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="scanneraction", options={"ordering": ["-pk"]},
        ),
        migrations.AlterField(
            model_name="scanseq",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Début du créneau"
            ),
        ),
    ]