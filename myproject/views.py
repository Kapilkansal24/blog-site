from django.shortcuts import render


def index(request):
    if request.session.get("email"):
        return render(request, "index.html")
    return render(request, "nav.html")