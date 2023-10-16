from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='member_photos')
    advance = models.IntegerField(default=0)
    current_meal_due = models.IntegerField(default=0)
    join_date = models.DateField()