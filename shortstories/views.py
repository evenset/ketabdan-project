from  django.shortcuts import get_object_or_404, render,redirect
from .models import ShortStory 
from .forms import ShortStoryForm
from  django import forms
from django.urls import reverse


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
            post.save()
            return redirect(reverse('shortstories:detail', args=(post.id,)))
    else:
        form = ShortStoryForm()
    return render (request, 'shortstories/shortstories_edit.html' , {'form': form})
