"""
URL configuration for landsay project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from landsay.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',layout1,name="layout1"),
    path('layout-1',layout1,name="layout1"),
    path('layout-2',layout2,name="layout2"),
    path('layout-3',layout3,name="layout3"),
    path('layout-4',layout4,name="layout4"),
    path('layout-5',layout5,name="layout5"),
    path('layout-6',layout6,name="layout6"),

    path('bloglist',bloglist,name="bloglist"),
    path('blogdetails',blogdetails,name="blogdetails"),

    path('login',login,name="login"),
    path('register',register,name="register"),
    path('resetpassword',resetpassword,name="resetpassword"),

    
]
