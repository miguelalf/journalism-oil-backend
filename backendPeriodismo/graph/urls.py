from django.urls import path

from . import views

urlpatterns = [
    path('lists', views.lists, name='lists'),
    path('corr/', views.corr, name='corr'),
]