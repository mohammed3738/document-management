# Generated by Django 4.2.5 on 2024-01-30 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_remove_financial2year_date_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financial2year',
            name='acknowledgement',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='financial2year',
            name='computation',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
