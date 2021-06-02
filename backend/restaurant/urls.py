from django.urls import path

from . import views

urlpatterns = [
    path('today-meal/', views.MenuAPIView.as_view())
]
