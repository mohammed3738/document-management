# Generated by Django 4.2.5 on 2024-01-30 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_acknowledgementfile_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acknowledgementfile',
            name='financial_year',
        ),
        migrations.RemoveField(
            model_name='computationfile',
            name='financial_year',
        ),
    ]
