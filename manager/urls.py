from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_member', views.add_member, name='add_member'),
    path('meal', views.meal, name='meal'),
    path('create_month', views.create_month, name='create_month'),
    path('update_meal', views.update_meal, name='update_meal'),
    path('add_joma', views.add_joma, name='add_joma'),
    path('add_bazar', views.add_bazar, name='add_bazar')
]
