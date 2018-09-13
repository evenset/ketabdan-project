from django.test import TestCase
from .models import ShortStory
from django.urls import reverse
from shortstories.models import User


def create_shortstories(author, status, title, body, publication_date):
    return ShortStory.objects.create(author=author, status=status, title=title, body=body, publication_date=publication_date)


class ShortstoriesIndexViewTests(TestCase):
    def  test_no_shortstories(self):
        response = self.client.get(reverse('shortstories:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No short stories available")

    def  test_current_shortstories(self):
        user_id = User.objects.create(id=1)
        current_shortstories = create_shortstories(author= user_id, status='p', title="Villete", body ="A romance written by Bronte Charlotte", publication_date='2000-08-25')
        url = reverse('shortstories:index')
        response = self.client.get(url)
        self.assertContains(response, current_shortstories.title)


class ShortstoriesDetailViewTests(TestCase):
    def  test_no_shortstory(self):
        response = self.client.get(reverse('shortstories:detail', args=(5756500,)))
        self.assertEquals(response.status_code, 404)

    def  test_current_shortstory(self):
        user_id = User.objects.create(id=1)
        current_shortstory = create_shortstories(author=user_id, status='p', title ="Villete", body="A romance written by Bronte Charlotte", publication_date='2000-08-25')
        response = self.client.get(reverse('shortstories:detail', args=(current_shortstory.id,)))
        self.assertContains(response, current_shortstory.title)


class Shortstories_Snippet_function(TestCase):
    def test_snippet_function(self):
        user_id = User.objects.create(id=1)
        current_shortstory = create_shortstories(author=user_id, status='p', title ="Villete", body="It was the hunter's first time outside Montana. He woke, stricken still with the hours-old vision of ascending through rose-lit cumulus, of houses and", publication_date='2000-08-25')
        snippet=current_shortstory.snippet()
        self.assertEqual(len(snippet),len(current_shortstory.body))

    def test_snippet_function_emptybody(self):
        user_id = User.objects.create(id=1)
        current_shortstory = create_shortstories(author=user_id, status='p', title ="Villete", body="It was the hunter's first time outside Montana. He woke, stricke", publication_date='2000-08-25')
        snippet=current_shortstory.snippet()
        self.assertEqual(len(snippet),len(current_shortstory.body))

    def test_snippet_function_largebody(self):
        user_id = User.objects.create(id=1)
        current_shortstory = create_shortstories(author=user_id, status='p', title ="Villete", body="It was the hunter's first time outside Montana. He woke, stricken still with the hours-old vision of ascending through rose-lit cumulus, of houses and maryam jhjkchjkhdjkahjkdkh", publication_date='2000-08-25')
        snippet=current_shortstory.snippet()
        self.assertTrue(len(snippet)==150)
