# Generated by Django 4.0.2 on 2024-03-19 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0005_remove_firereport_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalreport',
            old_name='loss_of_consciousness',
            new_name='loss_of_conciousness',
        ),
    ]
