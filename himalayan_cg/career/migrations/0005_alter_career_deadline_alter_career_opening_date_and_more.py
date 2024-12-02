# Generated by Django 5.1.3 on 2024-11-29 05:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0004_alter_career_deadline_alter_career_opening_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 6, 5, 24, 25, 435237, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='career',
            name='opening_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 29, 5, 24, 25, 435237, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='careerapply',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
