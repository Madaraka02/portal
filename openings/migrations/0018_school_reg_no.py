# Generated by Django 3.2.9 on 2021-11-12 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openings', '0017_auto_20211112_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='reg_no',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
