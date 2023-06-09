# Generated by Django 3.2.18 on 2023-03-29 12:45

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0004_alter_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
