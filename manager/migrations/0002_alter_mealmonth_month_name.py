# Generated by Django 4.2.5 on 2023-10-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealmonth',
            name='month_name',
            field=models.TextField(),
        ),
    ]
