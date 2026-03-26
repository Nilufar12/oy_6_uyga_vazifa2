"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.http import HttpResponse, HttpRequest


def index(request):
    return HttpResponse(
        '<h2 style="color: pink;'
        'text-align: center;'
        'background-color: lightblue;'
        'text-shadow: 2px 2px pink;">'
            '<a href="/about/"><i>Sahifamizga xush kelibsiz''</i></a>'
        '</h2>'
        '<div style="text-align: center";>'
            '<img src="https://www.w3schools.com/css/img_5terre.jpg";>'
        '</div>')


def about(request):
    return HttpResponse(
        '<h1 style="text-align: center;'
        'text-shadow: 2px 2px light grey;">'
        '<a href="/services/">Biz haqimizda</a></h1>'
        '<div style="text-align: center";>'
            '<img src="https://www.w3schools.com/css/img_forest.jpg";>'
        '</div>'
    )


def services(request):
    return HttpResponse(
        '<h1 style="text-align: center;">'
        '<a href="/detail/">Bizda quyidagi hizmatlar mavjud</a></h1>'
        '<div style="text-align: center;'
             'border: 5px solid #ff69b4; '
             'padding: 15px;'
             'border-image: url(border.png) 30 round;">'
             '<img src="https://www.w3schools.com/css/img_lights.jpg";>'
        '</div>'
    )


def detail(request):
    return HttpResponse('<h1><a href="/contact/">Batafsil ma\'lumot sahifasi</a></h1>')


def contact(request):
    return HttpResponse('<h1><a href="/team/">Biz bilan bo\'lanish</a></h1>')


def team(request):
    return HttpResponse('<h1><a href="">Bizning jamoamiz!!!</a></h1>')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('detail/', detail, name='detail'),
    path('contact/', contact, name='contact'),
    path('team/', team, name='team'),

]
