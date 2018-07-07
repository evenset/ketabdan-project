from django.db import models
class ShortStory(models.Model):
     status=(
        ('dr', 'Draft'),
        ('p' , 'Published'),
        ('b' , 'banned'),
        ('de', 'deleted'),
    )
    author =models.Foreignkey(user,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body = models.CharField(min_length=3500,Choices = status)
    publication_date = models.DateTimeField('date published')
