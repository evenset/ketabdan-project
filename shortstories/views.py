from django.shortcuts import render
from .models import ShortStory 

def index(request):
    shortstory_list = ShortStory.objects.all()
    context = {"short_story" : shortstory_list}
    return render(request, 'shortstories/index.html', context)
