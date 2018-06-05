from django.http import HttpResponse


def profile(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Hi, {request.user.username}!")
    else:
        return HttpResponse("Damn kids, get off my lawn!")
