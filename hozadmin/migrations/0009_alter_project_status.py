# Generated by Django 5.1.6 on 2025-02-20 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hozadmin', '0008_remove_project_days_remaining_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(blank=True, choices=[('Up Coming', 'Up Coming'), ('On Going UI', 'On Going UI'), ('On Going Dev', 'On Going Dev'), ('Completed', 'Completed')], default='Up Coming', max_length=255, null=True),
        ),
    ]
