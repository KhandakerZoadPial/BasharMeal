from django.db import models
from members.models import *


# Create your models here.

class Meal(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.TextField()
    number_of_meals = models.IntegerField(default=2)

class MealMonth(models.Model):
    month_name = models.TextField()
    year = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()
    members = models.ManyToManyField(Member, blank=True)
    all_meals = models.ManyToManyField(Meal, blank=True)


class Joma(models.Model):
    joma_by = models.ForeignKey(Member, on_delete=models.CASCADE)
    joma_month = models.ForeignKey(MealMonth, on_delete=models.CASCADE)
    joma_amount = models.IntegerField(default=0)
    joma_date = models.TextField(blank=True)
    joma_type = models.IntegerField(default=1) #1=meal 2=others


class Bazar(models.Model):
    bazar_by = models.ForeignKey(Member, on_delete=models.CASCADE)
    bazar_month = models.ForeignKey(MealMonth, on_delete=models.CASCADE)
    bazar_amount = models.IntegerField(default=0)
    bazar_details = models.TextField(blank=True)
    bazar_date = models.DateField(auto_now=True)