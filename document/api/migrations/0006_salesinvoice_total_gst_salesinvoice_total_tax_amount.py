# Generated by Django 4.2.6 on 2024-01-05 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_purchaseinvoice_total_gst_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesinvoice',
            name='total_gst',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='total_tax_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]