# Generated by Django 4.2.5 on 2023-10-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('picture', models.ImageField(upload_to='member_photos')),
                ('advance', models.IntegerField(default=0)),
                ('current_meal_due', models.IntegerField(default=0)),
                ('join_date', models.DateField()),
            ],
        ),
    ]