# Generated by Django 4.2.5 on 2023-11-07 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_assetspurchasedbill_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetspurchasedbill',
            name='month',
            field=models.CharField(choices=[('janauary', 'Janauary'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], max_length=50),
        ),
        migrations.AlterField(
            model_name='bankstatement',
            name='month',
            field=models.CharField(choices=[('janauary', 'Janauary'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], max_length=50),
        ),
        migrations.AlterField(
            model_name='interestcertificate',
            name='month',
            field=models.CharField(choices=[('janauary', 'Janauary'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], max_length=50),
        ),
    ]
