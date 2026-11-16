from django import urls
from . import views
from django.urls import path

app_name = 'directory_app'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('ticketform/', views.ticketform, name='ticketform'),
    path('ticketstatus/', views.ticketstatus, name='ticketstatus'),
    path('dashboard/', views.dashboard, name='dashboard'),
]