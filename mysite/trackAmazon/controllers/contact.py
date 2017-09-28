from django.shortcuts import render

def contact(request):
    if "email" in request.session:
        return render(request, "contact.html", {"Login": "True"})
    else:
        return render(request, "contact.html")