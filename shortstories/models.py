from django.db import models
from django.contrib.auth.models import User 
import math

def minute_count(text):
  words = text.split()
  number_of_words = len(words)
  return math.floor(number_of_words/250)

class ShortStory(models.Model):
    PUBLICATION_STATUS =(
        ('dr', 'Draft'),
        ('p' , 'Published'),
        ('b' , 'Banned'),
        ('de', 'Deleted'),
    )
    author = models.ForeignKey(User,on_delete = models.CASCADE) 
    title = models.CharField(max_length = 500)
    body = models.TextField(default= "No story written by the author")
    status = models.CharField(max_length = 1, choices = PUBLICATION_STATUS)
    publication_date = models.DateField()
    minutes_to_read = models.IntegerField(default=0)

    @property
    def snippet(self):
        return self.body[0:150]

    def save(self, *args, **kwargs):
        self.minutes_to_read = minute_count(self.body)
        super().save(*args, **kwargs) 
