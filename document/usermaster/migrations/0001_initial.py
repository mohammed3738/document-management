# Generated by Django 4.2.6 on 2023-12-28 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientVendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pan', models.CharField(max_length=100)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='VendorBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gst', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usermaster.clientvendor')),
            ],
        ),
    ]
