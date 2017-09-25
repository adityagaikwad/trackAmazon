from django.shortcuts import redirect


def logout(request):
    li = [key for key in request.session.keys()]
    for sesskey in li:
        del request.session[sesskey]
    return redirect("/")