# Generated by Django 5.1.1 on 2024-10-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_location", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="location",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
