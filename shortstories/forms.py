from  django import forms
from .models import ShortStory
from django.forms import widgets

class ShortStoryForm (forms.ModelForm):

    body = forms.CharField(min_length='3500', widget=widgets.Textarea)

    class Meta:
          model = ShortStory
          fields = ('author', 'title', 'status', 'body', 'publication_date')
