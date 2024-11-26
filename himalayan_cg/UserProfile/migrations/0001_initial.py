# Generated by Django 5.1.3 on 2024-11-22 08:58

import UserProfile.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=125)),
                ('image', models.ImageField(blank=True, upload_to=UserProfile.models.file_to_upload_profile_picture)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'user Profiles',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoardOfDirectors',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='UserProfile.profile')),
                ('rank', models.IntegerField(help_text='Lower the Rank, the higher the position is!', unique=True)),
                ('position', models.CharField(max_length=75)),
            ],
            options={
                'verbose_name': 'Board Member',
                'verbose_name_plural': 'Board of Directors',
                'ordering': ('rank',),
            },
            bases=('UserProfile.profile',),
        ),
        migrations.AddField(
            model_name='profile',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserProfile.team'),
        ),
    ]
