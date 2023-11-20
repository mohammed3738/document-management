# Generated by Django 4.2.5 on 2023-11-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_purchaseinvoice_debitnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditnote',
            name='gst_per',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='debitnote',
            name='gst_per',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseinvoice',
            name='booking_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseinvoice',
            name='gst_per',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseinvoice',
            name='is_reverse',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='booking_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='gst_per',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='is_reverse',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='creditnote',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='creditnote',
            name='cgst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='creditnote',
            name='cr_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='creditnote',
            name='sgst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='creditnote',
            name='tcs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='creditnote',
            name='tds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='debitnote',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='debitnote',
            name='cgst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='debitnote',
            name='cr_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='debitnote',
            name='sgst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='debitnote',
            name='tcs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='debitnote',
            name='tds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='cgst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='in_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='sgst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='tcs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='tds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesinvoice',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesinvoice',
            name='cgst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesinvoice',
            name='in_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesinvoice',
            name='sgst',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesinvoice',
            name='tcs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesinvoice',
            name='tds',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
