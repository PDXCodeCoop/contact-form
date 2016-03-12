from django.conf.urls import patterns, url
from django.core.mail import send_mail
from django.template.loader import render_to_string

from . import views

urlpatterns = [
            url('^$', views.index, name='index'),
            ]
