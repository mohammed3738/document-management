# Generated by Django 4.2.5 on 2024-01-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_financial2year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financial2year',
            name='date_field',
            field=models.DateField(blank=True, null=True),
        ),
    ]
