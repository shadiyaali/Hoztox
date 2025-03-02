# Generated by Django 5.1.6 on 2025-02-21 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hozadmin', '0017_alter_employee_designation_alter_project_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('Highest', 'Highest'), ('Medium', 'Medium'), ('Low', 'Low'), ('Lowest', 'Lowest')], default='Medium', max_length=20)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('attachments', models.FileField(blank=True, null=True, upload_to='task_files/')),
                ('assigned_employees', models.ManyToManyField(related_name='tasks', to='hozadmin.employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='hozadmin.project')),
            ],
        ),
    ]
