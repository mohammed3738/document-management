# Generated by Django 4.2.5 on 2023-10-23 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_bankdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='UdyamAadhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ua_number', models.CharField(max_length=255)),
                ('ua_login', models.CharField(max_length=255)),
                ('ua_password', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=500)),
                ('filling_freq', models.CharField(choices=[('monthly', 'Monthly'), ('half-year', 'Half-yearly'), ('quarterly', 'Quarterly'), ('yearly', 'Yearly')], max_length=100)),
                ('attachment', models.FileField(upload_to='')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
