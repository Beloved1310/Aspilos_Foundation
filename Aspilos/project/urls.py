from django.conf.urls import include, url

from project import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ResultsView

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/',views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('blog/', ResultsView.as_view(), name= 'blog'),


]


