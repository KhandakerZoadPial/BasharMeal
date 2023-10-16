# Generated by Django 4.2.5 on 2023-10-16 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('manager', '0006_joma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bazar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bazar_amount', models.IntegerField(default=0)),
                ('bazar_details', models.TextField(blank=True)),
                ('bazar_date', models.DateField(auto_now=True)),
                ('bazar_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
                ('bazar_month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.mealmonth')),
            ],
        ),
    ]
