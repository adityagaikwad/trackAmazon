from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^login$', login, name="login"),
    url(r'^register$', register, name="register")
]