# Generated by Django 4.2.5 on 2024-02-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_alter_taxfirm_date_of_incorporation'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
