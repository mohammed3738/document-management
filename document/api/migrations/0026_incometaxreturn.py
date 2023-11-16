# Generated by Django 4.2.5 on 2023-11-15 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_investmentstatement'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeTaxReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financial_year', models.DateField()),
                ('return_type', models.CharField(choices=[('computation-of-income', 'Computation-Of-Income'), ('financials', 'Financials'), ('income-tax-form', 'Income-Tax-Form'), ('income-tax-return', 'Income-Tax-Return'), ('tax-audit', 'Tax-Audit'), ('cma', 'CMA'), ('auditors-report', 'Auditors-Report')], max_length=100)),
                ('attachment', models.FileField(upload_to='')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
