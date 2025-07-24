from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 725d339f is the polls index.")