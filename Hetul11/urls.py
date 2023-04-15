"""Hetul16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

# urlpatterns = [
    # re_path("", views.index, name="shophome"),
    # re_path("search/", views.search, name="search"),
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index ,name="Shop home"),
    path('search/', views.search,name="Search"),
    path('iphone13/', views.iphone13,name="Apple"),
    path('nothing/', views.nothing,name="nothing"),
    path('zflip/', views.zflip,name="zflip"),
    path('motoe40/', views.motoe40,name="motoe40"),
    path('airpods/', views.airpods,name="airpods"),
    path('mivi/', views.mivi,name="mivi"),
    path('noice/', views.noice,name="noice"),
    path('boat131/', views.boat131,name="boat131"),
    path('trackprices/', views.trackprices,name="comaprision"),
]
