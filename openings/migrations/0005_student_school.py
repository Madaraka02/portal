# Generated by Django 3.2.9 on 2021-11-10 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openings', '0004_remove_student_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
