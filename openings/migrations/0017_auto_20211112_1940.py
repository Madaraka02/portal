# Generated by Django 3.2.9 on 2021-11-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openings', '0016_alter_jobs_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]