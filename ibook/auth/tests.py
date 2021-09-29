from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.


class AuthenticatorTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "dangnhtester", "dangnhtester@email.com", "p4s$word")
        self.client = APIClient()
        self.login_url = reverse('LoginView')
        self.helloworld_url = reverse('HelloWorldView')
        self.extractor_url = reverse('ExtractTokenView')
        self.access_token = self.client.post(
            self.login_url,
            {'username': 'dangnhtester', 'password': 'p4s$word'}
        ).json()['access']

    def test_login_return_jwt(self):
        """
        the login view return an access token and a refresh token
        """

        credentials = {
            'username': 'dangnhtester',
            'password': 'p4s$word',
        }

        response = self.client.post(self.login_url, credentials)

        print('\n\n1. the login view return an access token and a refresh token')
        print(response.status_code)
        print(response.json())

        self.assertEqual(response.status_code, 200)
        self.assertTrue('access' in response.json().keys())
        self.assertTrue('refresh' in response.json().keys())

    def test_bad_login_return_jwt(self):
        """
        the login view do not return a token if we use bad credentials
        """

        credentials = {
            'username': 'dangnhtester',
            'password': 'p4s$wordFake',
        }

        response = self.client.post(self.login_url, credentials)

        print('\n\n2. the login view do not return a token if we use bad credentials')
        print(response.status_code)
        print(response.json())

        self.assertEqual(response.status_code, 401)

    def test_return_hello_world_view(self):
        """
        the hello world view return hello world
        """

        expected_response = {'message': 'Hello World'}
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.helloworld_url)

        print('\n\n3. the hello world view return hello world')
        print(response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)

    def test_extractor_return_username_and_password(self):
        """
        the extract token view return username and password
        """

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.extractor_url)

        print('\n\n4. the extract token view return username and password')
        print(response.json())

        self.assertEqual(response.status_code, 200)
        self.assertTrue('username' in response.json().keys())
        self.assertTrue('password' in response.json().keys())
