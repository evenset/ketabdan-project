from django.db import models


class Podcast(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="Name of the podcast")
    description = models.CharField(max_length=1000, blank=True, help_text="A short description of the podcast")
    avatar = models.ImageField(upload_to='podcasts/avatars/', null=True)
    itunes_link = models.URLField(blank=True, help_text="The link to your iTunes channel")
    blubrry_link = models.URLField(blank=True, help_text="The link to you Blubrry channel")

    def __str__(self):
        return self.name


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text="Title of your episode")
    story = models.TextField(blank=True)
    file = models.FileField(upload_to='podcasts/episodes/files/')
    avatar = models.ImageField(upload_to='podcasts/episodes/', null=True)
    release_date = models.DateTimeField(auto_now=True, editable=False)
    soundcloud_link = models.URLField(blank=True, help_text="The link to the episode soundcloud")

    def __str__(self):
        return self.title





