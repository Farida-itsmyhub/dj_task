# Generated by Django 4.0.1 on 2022-02-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_alter_table_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='max_speed',
            field=models.CharField(max_length=200),
        ),
    ]
