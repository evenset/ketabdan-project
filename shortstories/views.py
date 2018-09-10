from django.shortcuts import get_object_or_404, render
from .models import ShortStory 


def index(request):
    shortstory_list = ShortStory.objects.order_by('publication_date')
    return render(request, 'shortstories/index.html', {'shortstories' :shortstory_list})

def detail(request, shortstory_id):
    shortstory =  get_object_or_404(ShortStory, pk=shortstory_id)
    return render(request,'shortstories/detail.html',{'shortstory':shortstory})
