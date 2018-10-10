from django.test import TestCase,Client
from .models import ShortStory
from django.urls import reverse
from shortstories.models import User,minute_count
from .forms import ShortStoryForm
from django.contrib.auth.models import User


def create_shortstories(author, status, title, body, publication_date):
    return ShortStory.objects.create(author=author, status=status, title=title, body=body, publication_date=publication_date)


class ShortstoriesIndexViewTests(TestCase):
    def  test_no_shortstories(self):
        response = self.client.get(reverse('shortstories:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No short stories available")

    def  test_current_shortstories(self):
        user= User.objects.create(id=1)
        current_shortstories = create_shortstories(author= user, status='p', title="Villete", body ="A romance written by Bronte Charlotte", publication_date='2000-08-25')
        url = reverse('shortstories:index')
        response = self.client.get(url)
        self.assertContains(response, current_shortstories.title)


class ShortstoriesDetailViewTests(TestCase):
    def  test_no_shortstory(self):
        response = self.client.get(reverse('shortstories:detail', args=(5756500,)))
        self.assertEquals(response.status_code, 404)

    def  test_current_shortstory(self):
        user= User.objects.create(id=1)
        current_shortstory = create_shortstories(author=user, status='p', title="Villete", body="A romance written by Bronte Charlotte", publication_date='2000-08-25')
        response = self.client.get(reverse('shortstories:detail', args=(current_shortstory.id,)))
        self.assertContains(response, current_shortstory.title)


class ShortstoriesSnippetFunctionTests(TestCase):
    def test_snippet_function(self):
        user= User.objects.create(id=1)
        current_shortstory = create_shortstories(author=user, status='p', title="Villete", body="It was the hunter's first time outside Montana. He woke, stricken still with the hours-old vision of ascending through rose-lit cumulus, of houses and", publication_date='2000-08-25')
        snippet=current_shortstory.snippet
        self.assertEqual(len(snippet),len(current_shortstory.body))

    def test_snippet_function_emptybody(self):
        user= User.objects.create(id=1)
        current_shortstory = create_shortstories(author=user, status='p', title="Villete", body="It was the hunter's first time outside Montana. He woke, stricke", publication_date='2000-08-25')
        snippet=current_shortstory.snippet
        self.assertEqual(snippet,current_shortstory.body)

    def test_snippet_function_largebody(self):
        user = User.objects.create(id=1)
        current_shortstory = create_shortstories(author=user, status='p', title="Villete", body="It was the hunter's first time outside Montana. He woke, stricken still with the hours-old vision of ascending through rose-lit cumulus, of houses and maryam jhjkchjkhdjkahjkdkh", publication_date='2000-08-25')
        snippet=current_shortstory.snippet
        self.assertTrue(len(snippet)==150)

class ShortstoriesMinuteCountFunctionTests(TestCase):
    def test_minute_count_function_emptytext(self):
        user= User.objects.create(id=1)
        current_shortstory = create_shortstories(author=user, status='p', title="Villete", body="", publication_date='2000-08-25')
        current_shortstory.minute_to_read = minute_count(current_shortstory.body)
        self.assertTrue(current_shortstory.minute_to_read==0)

    def test_minute_count_function_shorttext(self):
        user= User.objects.create(id=1)
        current_shortstory = create_shortstories(author=user, status='p', title="Villete", body="It was the hunter's first time outside Montana. He woke", publication_date='2000-08-25')
        current_shortstory.minute_to_read = minute_count(current_shortstory.body)
        self.assertTrue(current_shortstory.minute_to_read==0)

    def test_minute_count_function_longtext(self):
        user= User.objects.create(id=1)
        current_shortstory = create_shortstories(author=user, status='p', title="Villete", body="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, It was the hunter's first time outside Montana. He woke, stricken still with the hours-old vision of ascending through rose-lit cumulus, of houses and mdhojdhudhfdhfu jhdijhdufig fbufh jhduigfiuygfuigf jgdydgyfuefoihfui dgdfuydgfugduidgyuidv  idguciydgyidgyidgydg hgddcydgchdbvyidgdidjb Forgiven? No. I am a bad, low woman; I despise myself and don't attempt to justify myself. It's not my husband but myself I have deceived. And not only just now; I have been deceiving myself for a long time. My husband may be a good, honest man, but he is a flunkey! I don't know what he does there, what his work is, but I know he is a flunkey! I was twenty when I was married to him. I have been tormented by curiosity; I wanted something better. 'There must be a different sort of life,' I said to myself. I wanted to live! To live, to live!... I was fired by curiosity ... you don't understand it, but, I swear to God, I could not control myself; something happened to me: I could not be restrained. I told my husband I was ill, and came here.... And here I have been walking about as though I were dazed, like a mad creature; and now I have become a vulgar, contemptible woman whom any one may despise.", publication_date='2000-08-25')
        current_shortstory.minute_to_read = minute_count(current_shortstory.body)
        self.assertTrue(current_shortstory.minute_to_read==1)

class ShortStoryFormTests(TestCase):
    def test_ShortStory_invalid(self):
        user= User.objects.create(id=1)
        form = ShortStoryForm(data={'author':'', 'status':'', 'title':"", 'body':"", 'publication_date':''})
        self.assertFalse(form.is_valid())

    def test_ShortStory_valid(self):
        user = User.objects.create(id=1)
        form = ShortStoryForm(data={'author':user.id, 'status':'p', 'title':"Villette", 'body':"a"*3501, 'publication_date':'2000-08-30'})
        self.assertTrue(form.is_valid())

class ShortStoriesCreateViewTests(TestCase):

    def setUp(self):
        """
        Set up is called before running these tests in the main class
        """
        user = User.objects.create(username='testuser')
        user.set_password('12345') # you need to call set password to store the hash in DB
        user.save()

    def  test_no_new_shortstory(self):
         response = self.client.get(reverse('shortstories:detail', args=(7645392,)))
         self.assertEquals(response.status_code, 404)

    def test_loggedin_users_see_the_form(self):
        login = self.client.login(username='testuser', password='12345')
        self.assertTrue(login) 
        response = self.client.get(reverse('shortstories:create'))
        self.assertEquals(response.status_code, 200)
    
    def test_unauthenticated_users_get_redirected(self):
        response = self.client.get(reverse('shortstories:create'))
        expected_url = reverse('account_login') + "?next=" + reverse('shortstories:create')
        self.assertRedirects(response, expected_url, status_code=302, target_status_code=200)
