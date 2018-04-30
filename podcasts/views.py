from django.http import HttpResponse


def index(request):
    return HttpResponse("You're seeing the lists of available podcasts")
