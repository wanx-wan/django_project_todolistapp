"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import authenticate, login as authlogin
from django.contrib.auth import logout as authlogout
from django.shortcuts import render, redirect
from django.urls import path, include


def home(req):
    return render(req, 'home.html')


def login(req):
    if req.method == 'POST':
        print("ข้อมูลที่รับมา")
        # for u in User.objects.all():
        #    print(u.username)
        # print(req.POST)
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            authlogin(req, user)
            return redirect('/')
        else:
            return render(req, 'login.html', {"message": "ไม่มีผู้ใช้อยู่จริง"})
    return render(req, 'login.html')


def logout(req):
    authlogout(req)
    return redirect('/')


urlpatterns = [
    path("", home),
    path("login", login),
    path("logout", logout),
    path("admin/", admin.site.urls),
    path('myapp/', include('myapp.urls')),
]

