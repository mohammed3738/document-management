# Generated by Django 4.2.5 on 2024-02-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_company_gst_company_pan_alter_pan_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerdetails',
            name='share',
            field=models.IntegerField(default=100),
        ),
    ]
