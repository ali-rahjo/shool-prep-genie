# Generated by Django 5.0.7 on 2024-10-15 17:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Parent", "0003_writemsg_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="leave",
            name="date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Date Sent"
            ),
        ),
    ]
