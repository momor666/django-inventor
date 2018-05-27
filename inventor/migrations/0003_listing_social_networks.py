# Generated by Django 2.0.5 on 2018-05-27 22:23

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0002_remove_listing_social_networks'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='social_networks',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, verbose_name='social networks'),
        ),
    ]