"""Am_I_Available URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
urlpatterns = [
    path("",views.home1,name="home1"),
    path("home",views.home,name="home"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path('logout',views.logout,name="logout"),
    path("Search",views.search,name="search"),
    path('Faculty_Registration',views.Faculty_registration,name="Registration"),
    path('updatestatus',views.updatestatus,name="updatestatus"),
    path('forgotpassword',views.forgotpassword,name="forgotpassword"),
]