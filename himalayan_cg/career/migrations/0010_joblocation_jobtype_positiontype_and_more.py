# Generated by Django 5.1.3 on 2024-11-26 08:32

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0009_alter_career_created_at_alter_career_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_location', models.CharField(help_text='(E.g. On-Site, Remote, Hybrid)', max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(help_text='(E.g. Full Time, Part Time)', max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='PositionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_type', models.CharField(help_text='E.g. Internship, Entry Level, Mid Level, Senior Level', max_length=75)),
            ],
        ),
        migrations.AlterModelOptions(
            name='career',
            options={'verbose_name': 'Vacancy', 'verbose_name_plural': 'Vacancies'},
        ),
        migrations.AlterModelOptions(
            name='careerapply',
            options={'verbose_name': 'Application', 'verbose_name_plural': 'Applications'},
        ),
        migrations.AlterField(
            model_name='career',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 26, 8, 32, 10, 641480, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='career',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 3, 8, 32, 10, 641480, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='career',
            name='job_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='career.joblocation'),
        ),
        migrations.AlterField(
            model_name='career',
            name='job_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='career.jobtype'),
        ),
        migrations.AlterField(
            model_name='career',
            name='position_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='career.positiontype'),
        ),
    ]