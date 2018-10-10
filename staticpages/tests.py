class ShortStoriesCreateLIinkTests(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345') 
        user.save()

    def test_loggedin_users_see_the_link(self):
        login = self.client.login(username='testuser', password='12345')
        self.assertTrue(login) 
        response = self.client.get(reverse('shortstories:create'))
        expected_url = reverse('account_login') + "?next=" + reverse('shortstories:create')
        self.assertRedirects(response, expected_url, status_code=302, target_status_code=200)
