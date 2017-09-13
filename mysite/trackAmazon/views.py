from django.shortcuts import render

def index(request):

    di = {"ki": "hi", 2 : {"ko": 2, "q": 3}}
    return render(request, "index.html", di)