from django.http import HttpResponse
from .models import ShortStory 

def index(request):

    return  HttpResponse("You Will See ShortStory here")



