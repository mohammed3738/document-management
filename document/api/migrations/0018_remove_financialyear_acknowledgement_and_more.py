# Generated by Django 4.2.5 on 2024-01-30 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_financialyear_acknowledgement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financialyear',
            name='acknowledgement',
        ),
        migrations.RemoveField(
            model_name='financialyear',
            name='computation',
        ),
        migrations.CreateModel(
            name='ComputationFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='computation_files/')),
                ('financial_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.financialyear')),
            ],
        ),
        migrations.CreateModel(
            name='AcknowledgementFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='acknowledgement_files/')),
                ('financial_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.financialyear')),
            ],
        ),
        migrations.AddField(
            model_name='financialyear',
            name='acknowledgement',
            field=models.ManyToManyField(blank=True, to='api.acknowledgementfile'),
        ),
        migrations.AddField(
            model_name='financialyear',
            name='computation',
            field=models.ManyToManyField(blank=True, to='api.computationfile'),
        ),
    ]
