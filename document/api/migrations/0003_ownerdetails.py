# Generated by Django 4.2.5 on 2023-10-20 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('share', models.CharField(max_length=255)),
                ('pan', models.CharField(max_length=255)),
                ('aadhar', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
