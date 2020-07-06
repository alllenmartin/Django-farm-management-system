from django.contrib import admin
from django.urls import path
from . import views as user_views

app_name = 'app'
urlpatterns = [
     path('farm', user_views.farm_form, name='farm'),
     path('users', user_views.registered_users, name='users'),
     path('activate/user/<int:user_id>', user_views.user_activate, name='activate_user'),
     path('deactivate/user/<int:user_id>', user_views.user_deactivate, name='deactivate_user'),
    
]
