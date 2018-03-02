"""SNMP0001 URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from . import views

app = 'connector'
urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.my_login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^info/', include('info.urls')),
    url(r'^connector/', include('connector.urls')),
    url(r'^optic-network/', include('optic_network.urls')),
    url(r'^telebot/', include('helper_bot.urls')),
    #url(r'^sktv/', include('sktv.urls')),

    #url(r'^connector/', include('connector.urls')),
]
