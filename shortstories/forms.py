from django import forms
from .models import ShortStory


class ShortStoryForm (form.ModELForm):

    class Meta:
          model = ShortStory
          #here should be field(s) which should end up in our form but it is not mentioned in the task.
