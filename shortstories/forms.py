from django import forms
from .models import ShortStory


class ShortStoryForm (forms.ModelForm):

    body = forms.CharField(widget =forms.Textarea(attrs={'maxlength':'35000',}))

    class Meta:
          model = ShortStory
          fields = ('author','title', 'status','body','publication_date', 'minutes_to_read')
