from django.contrib import admin
from django.urls import path
from . import views as user_views

urlpatterns = [
     path('profile', user_views.user_profile, name='profile'),
     path('table', user_views.user_table, name='table'),
]
