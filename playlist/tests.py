from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .views import MusicViewSet
from rest_framework.test import APIClient


class TestMusic(APITestCase):
    def setUp(self):
        self.view = MusicViewSet.as_view({'get': 'list'})
        self.uri = '/musics/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client = APIClient()
    
    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )

    def test_list(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.'
                         )
        
    def test_create(self):
        self.client.login(username="test", password="test")
        params = {
            "user": 1,
            "author": "labrinth",
            "name": "Never felt so alone",
            "musical_genre": "Pop"
            }   
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         f'Expected Response Code 201, received {response.status_code} instead.'
                         )

