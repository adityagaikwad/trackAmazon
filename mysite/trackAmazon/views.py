from django.shortcuts import render

# Create your views here.

def index(request):

    di = {"ki":"hi", 2: "jo"}
    return render(request, "index.html", di)