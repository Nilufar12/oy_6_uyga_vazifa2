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
    return HttpResponse('<h2><a href="/about/">Sahifamizga xush kelibsiz</a></h2>')


def about(request):
    return HttpResponse('<h1><a href="/services/">Biz haqimizda</a></h1>')


def services(request):
    return HttpResponse('<h1><a href="/detail/">Bizda quyidagi hizmatlar mavjud</a></h1>')


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
