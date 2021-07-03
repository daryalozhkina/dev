from django.contrib import admin
from django.urls import path, include

app_name = 'mainapp'

urlpatterns = [
    path('', include('mainapp.urls', namespace='main')),
    path('about/', include('mainapp.about', namespace='about')),
    path('auth/', include('authapp.urls',  namespace='auth')),
]
