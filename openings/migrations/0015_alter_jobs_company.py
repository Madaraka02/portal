# Generated by Django 3.2.9 on 2021-11-12 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openings', '0014_alter_jobs_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='openings.company'),
        ),
    ]
