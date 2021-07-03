from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('login/', 'authapp.login', namespace='login'),
    path('logout/', 'authapp.logout', namespace='logout'),
]
