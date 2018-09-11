from django.test import TestCase
from .models import ShortStory
from django.urls import reverse
from shortstories.models import User


def create_shortstories(author, status,title,body,publication_date):
    return ShortStory.objects.create(author=author, status=status, title=title, body=body, publication_date=publication_date)


class shortstoriesIndexViewTests(TestCase):
    def  test_no_shortstories(self):
        response = self.client.get(reverse('shortstories:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No short stories available")

    def  test_current_shortstories(self):
        user_id = User.objects.create(id=1)
        current_shortstories = create_shortstories(author= user_id, status ='p', title="Villete", body ="A romance written by Bronte Charlotte", publication_date ='2000-08-25')
        url = reverse('shortstories:index')
        response = self.client.get(url)
        self.assertContains(response, current_shortstories.title)


class shortstoriesDetailViewTests(TestCase):
    def  test_no_shortstory(self):
        response = self.client.get(reverse('shortstories:detail', args=(5756500,)))
        self.assertEquals(response.status_code, 404)

    def  test_current_shortstory(self):
        user_id = User.objects.create(id=1)
        current_shortstory = create_shortstories(author=user_id, status='p', title ="Villete", body="A romance written by Bronte Charlotte", publication_date='2000-08-25')
        response = self.client.get(reverse('shortstories:detail', args=(current_shortstory.id,)))
        self.assertContains(response, current_shortstory.title)
