# Generated by Django 3.2.9 on 2021-11-17 20:43

from django.db import migrations, models
import openings.models


class Migration(migrations.Migration):

    dependencies = [
        ('openings', '0032_student_transcript'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='transcript',
            field=models.FileField(null=True, upload_to=openings.models.file_path),
        ),
    ]