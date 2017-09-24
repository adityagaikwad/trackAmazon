from django.shortcuts import render

def works(request):
    return render(request, "works.html")