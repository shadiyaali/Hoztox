# Generated by Django 5.1.6 on 2025-02-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hozadmin', '0010_client_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15, null=True)),
                ('employee_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('join_date', models.DateField(blank=True, max_length=15, null=True)),
                ('username', models.CharField(blank=True, max_length=15, null=True)),
                ('password', models.CharField(blank=True, max_length=15, null=True)),
                ('department', models.CharField(blank=True, choices=[('IT Management', 'IT Management'), ('Marketing', 'Marketing')], max_length=200, null=True)),
                ('Designation', models.CharField(blank=True, choices=[('UI/UX Design', 'UI/UX Design'), ('Website Design', 'Website Design'), ('Web App Development', 'Web App Development'), ('SEO', 'SEO'), ('Social Media', 'Social Media'), ('Backend Development', 'Backend Development'), ('Digital Marketing', 'Digital Marketing'), ('Other', 'Other')], max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=15, null=True)),
                ('religion', models.CharField(blank=True, max_length=15, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=15, null=True)),
                ('emergency_contact', models.CharField(blank=True, max_length=15, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=15, null=True)),
                ('acc_no', models.CharField(blank=True, max_length=15, null=True)),
                ('ifsc', models.CharField(blank=True, max_length=15, null=True)),
                ('pan', models.CharField(blank=True, max_length=15, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
