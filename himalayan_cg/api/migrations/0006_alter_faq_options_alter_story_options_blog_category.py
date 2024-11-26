# Generated by Django 5.1.3 on 2024-11-26 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_category_options_organizationdetail_logo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'FAQ', 'verbose_name_plural': 'FAQs'},
        ),
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name_plural': 'Stories'},
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_category', to='api.category'),
        ),
    ]
