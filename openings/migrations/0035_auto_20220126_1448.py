# Generated by Django 3.2.9 on 2022-01-26 14:48

from django.db import migrations, models
import openings.models


class Migration(migrations.Migration):

    dependencies = [
        ('openings', '0034_studentcertifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='upload_certifications',
            field=models.FileField(blank=True, null=True, upload_to=openings.models.cert_path),
        ),
        migrations.AddField(
            model_name='application',
            name='upload_cv',
            field=models.FileField(blank=True, null=True, upload_to=openings.models.cert_path),
        ),
    ]
