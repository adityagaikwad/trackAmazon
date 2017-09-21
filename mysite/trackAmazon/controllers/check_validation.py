from django.shortcuts import render
from ..forms import *


def login(request):
    if "username" in request.session:
        return True
    else:
        return False