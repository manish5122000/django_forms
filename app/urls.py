from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.MyFormView, name='home'),
]