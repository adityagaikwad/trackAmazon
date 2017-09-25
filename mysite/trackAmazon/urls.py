from django.conf.urls import url
from .controllers.index import *
from .controllers.login import *
from .controllers.register import *
from .controllers.contact import *
from .controllers.works import *
from .controllers.logout import *

urlpatterns = [
    url(r'^$', index_req, name="index"),
    url(r'^login$', login, name="login"),
    url(r'^register$', register, name="register"),
    url(r'^contact$', contact, name="contact"),
    url(r'^how-it-works', works, name="works"),
    url(r'^logout', logout, name="logout")
]