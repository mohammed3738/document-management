# Generated by Django 4.2.5 on 2024-02-01 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_remove_yourmodel_acknowledgement_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yourmodel',
            old_name='date',
            new_name='from_date',
        ),
        migrations.AddField(
            model_name='yourmodel',
            name='client_review',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='yourmodel',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
        migrations.AddField(
            model_name='yourmodel',
            name='frequency',
            field=models.CharField(blank=True, choices=[('monthly', 'Monthly'), ('half-year', 'Half-yearly'), ('quarterly', 'Quarterly'), ('yearly', 'Yearly')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='yourmodel',
            name='month',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='yourmodel',
            name='remark',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='yourmodel',
            name='return_type',
            field=models.CharField(blank=True, choices=[('gstr-1', 'GSTR-1'), ('gstr-3b', 'GSTR-3B'), ('gstr-4', 'GSTR-4'), ('gstr-5', 'GSTR-5'), ('gstr-5a', 'GSTR-5A'), ('gstr-6', 'GSTR-6'), ('gstr-7', 'GSTR-7'), ('gstr-8', 'GSTR-8'), ('gstr-9', 'GSTR-9'), ('gstr-10', 'GSTR-10'), ('gstr-11', 'GSTR-11'), ('cmp-8', 'CMP-8'), ('itc-04', 'ITC-04'), ('income-tax', 'Income-Tax'), ('tax-audit', 'Tax-Audit'), ('sft', 'SFT')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='yourmodel',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]