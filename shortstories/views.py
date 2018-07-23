from django.http import HttpResponse
from ketabdan-project.shortstories.models import ShortStory 

def index(request):
    ShortStory_List= ShortStory.objects.all()
    return  HttpResponse(ShortStory_List)



