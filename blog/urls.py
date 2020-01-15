# from django.contrib import admin
from django.urls import path
from blog import views
# import blog

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]