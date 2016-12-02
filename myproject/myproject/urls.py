"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from polls import views as polls_views
from django.contrib import admin

urlpatterns = [
    #url(r'^$',polls_views.index),
    #url(r'^$', polls_views.home),
    url(r'^$',polls_views.search),
    url(r'^log/$',polls_views.image, name='index'),
    url(r'^pic/$',polls_views.pic, name='index'),
    url(r'^back/$',polls_views.back),
    #url(r'^admin/', admin.site.urls),
    #url(r'^polls/', include('polls.urls')),
]