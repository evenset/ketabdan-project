from django import forms
from .models import ShortStory


class ShortStoryForm (forms.ModelForm):

    class Meta:
          model = ShortStory
          fields = ('author','title', 'status','body')
