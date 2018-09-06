from django.shortcuts import render
from .models import ShortStory 

def index(request):
    shortstory_list = ShortStory.objects.order_by('publication_date')
    context = {"shortstories" : shortstory_list}
    return render(request, 'shortstories/index.html', context)
