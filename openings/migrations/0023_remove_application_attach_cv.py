# Generated by Django 3.2.9 on 2021-11-14 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openings', '0022_auto_20211114_0528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='attach_cv',
        ),
    ]