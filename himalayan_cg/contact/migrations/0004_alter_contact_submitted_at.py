# Generated by Django 5.1.3 on 2024-11-26 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_options_alter_contact_submitted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='submitted_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 26, 17, 27, 19, 56660)),
        ),
    ]
