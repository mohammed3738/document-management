# Generated by Django 4.2.5 on 2024-02-17 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_alter_ownerdetails_share'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ownerdetails',
            old_name='share',
            new_name='default_share',
        ),
    ]
