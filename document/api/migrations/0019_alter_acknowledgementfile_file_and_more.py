# Generated by Django 4.2.5 on 2024-01-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_remove_financialyear_acknowledgement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acknowledgementfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='computationfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
