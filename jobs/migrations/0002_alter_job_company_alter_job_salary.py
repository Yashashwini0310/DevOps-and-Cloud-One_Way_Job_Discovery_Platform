# Generated by Django 4.2.20 on 2025-03-20 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="company",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="job",
            name="salary",
            field=models.PositiveIntegerField(),
        ),
    ]
