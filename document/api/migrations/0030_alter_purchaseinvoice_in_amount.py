# Generated by Django 4.2.5 on 2023-11-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_purchaseinvoice_in_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='in_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]