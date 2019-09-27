"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from movieapp.views import create_movie_list
from MyApp.views import home,add_to_do,delete_to_do

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_movie_list, name='create'),
    path('add/', add_to_do, name='add'),
    path('delete/<int:item_id>', delete_to_do, name='delete'),
    path('admin/', admin.site.urls),
]
