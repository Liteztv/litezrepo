# Generated by Django 4.0.2 on 2024-03-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0008_alter_chemicalreport_environment_affected_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='firereport',
            name='Test',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
