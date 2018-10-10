from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE) 
    display_name = models.CharField(max_length = 200)
    biography = models.TextField
