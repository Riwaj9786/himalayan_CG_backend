# Generated by Django 5.1.3 on 2024-11-26 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0002_proposal_project_year'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='proposal',
            unique_together={('email', 'project_year')},
        ),
    ]
