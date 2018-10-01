from  django.shortcuts import get_object_or_404, render,redirect
from .models import ShortStory 
from .forms import ShortStoryForm
from  django import forms
from  django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    shortstory_list = ShortStory.objects.order_by('publication_date')
    return render(request, 'shortstories/index.html', {'shortstories' :shortstory_list})

def detail(request, shortstory_id):
    shortstory =  get_object_or_404(ShortStory, pk=shortstory_id)
    return render(request,'shortstories/detail.html',{'shortstory':shortstory})

@login_required
def create(request):
    if request.method == "POST":
       form = ShortStoryForm(request.POST)
       if form.is_valid():
            shortstory = form.save(commit=False)
            shortstory.save()
            return redirect(reverse('shortstories:detail', args=(shortstory.id,)))
    else:
        form = ShortStoryForm()
    return render (request, 'shortstories/shortstories_edit.html', {'form':form})
