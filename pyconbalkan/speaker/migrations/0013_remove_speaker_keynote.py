# Generated by Django 2.2.4 on 2019-08-27 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0012_auto_20190827_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='keynote',
        ),
    ]
