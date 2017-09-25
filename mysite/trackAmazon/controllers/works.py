from django.shortcuts import render

def works(request):
    if "email" in request.session:
        return render(request, "works.html", {"Login": "True"})
    else:
        return render(request, "works.html")