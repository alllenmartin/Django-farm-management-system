from django.contrib import admin
from django.urls import path
from . import views as user_views

urlpatterns = [
     path('farm', user_views.farm_form, name='farm'),
    
]
