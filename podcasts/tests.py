from django.test import TestCase
from .models import Podcast, Episode
from django.urls import reverse


class PodcastModelTests(TestCase):

    def test_dummy(self):
        self.assertIs(True, True)


def create_podcast(name, description, avatar, itunes_link, blubrry_link):
    return Podcast.objects.create(name=name, description=description , avatar=avatar, itunes_link = itunes_link, blubrry_link = blubrry_link )


class PodcastsIndexViewTests(TestCase):
    def  test_no_podcasts(self):
        response = self.client.get(reverse('podcasts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No podcast available")

    def  test_current_podcasts(self):
        current_podcasts = create_podcast(name= "This American Life", description= "This American Life is an American weekly hour-long radio program" , avatar= "" , itunes_link = "", blubrry_link = "" )
        url = reverse('podcasts:index')
        response = self.client.get(url)
        self.assertContains(response, current_podcasts.name)


class PodcastDetailViewTests(TestCase):
    def  test_no_podcast(self):
        response = self.client.get(reverse('podcasts:detail', args=(5756500,)))
        self.assertEquals(response.status_code, 404)

    def  test_current_podcast(self):
        current_podcast= create_podcast(name= "This American Life", description= "This American Life is an American weekly hour-long radio program" , avatar= "" , itunes_link = "", blubrry_link = "" )
        response = self.client.get(reverse('podcasts:detail', args=(current_podcast.id,)))
        self.assertContains(response, current_podcast.name)
