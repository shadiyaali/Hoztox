# Generated by Django 5.1.6 on 2025-02-21 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hozadmin', '0014_employee_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
