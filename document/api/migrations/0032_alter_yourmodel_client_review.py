# Generated by Django 4.2.5 on 2024-02-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_alter_yourmodel_client_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourmodel',
            name='client_review',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
