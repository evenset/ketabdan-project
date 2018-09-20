from django.shortcuts import get_object_or_404, render,redirect
from .models import ShortStory 
from .forms import ShortStoryForm
from  django import forms



def index(request):
    shortstory_list = ShortStory.objects.order_by('publication_date')
    return render(request, 'shortstories/index.html', {'shortstories' :shortstory_list})

def detail(request, shortstory_id):
    shortstory =  get_object_or_404(ShortStory, pk=shortstory_id)
    return render(request,'shortstories/detail.html',{'shortstory':shortstory})

def create(request):
    if request.method == "POST":
       form = ShortStoryForm(request.POST)
       if form.is_valid():
            post = form.save(commit=False)
            post.body = forms.CharField(max_length = 3500)
            post.save()
            return redirect('detail/', pk=post.pk)
    else:
        form = ShortStoryForm()
    return render (request, 'shortstories/shortstories_edit.html' , {'form': form})
