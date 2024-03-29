# Generated by Django 4.2.4 on 2024-01-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_salesinvoice_total_gst_salesinvoice_total_tax_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetspurchasedbill',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assetspurchasedbill',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bankstatement',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bankstatement',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='interestcertificate',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interestcertificate',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='investmentstatement',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loanvoucher',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loanvoucher',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tdscertificate',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
