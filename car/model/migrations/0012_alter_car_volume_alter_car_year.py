# Generated by Django 5.0.4 on 2024-04-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0011_alter_marka_marka_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='volume',
            field=models.FloatField(default=0.8),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.DateField(default=2024),
        ),
    ]
