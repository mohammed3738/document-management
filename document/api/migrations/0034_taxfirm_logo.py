# Generated by Django 4.2.5 on 2024-02-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_taxfirm_gst_taxfirm_pan_taxfirm_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxfirm',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]