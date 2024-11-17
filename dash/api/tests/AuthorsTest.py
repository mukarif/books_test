from datetime import datetime

from main.models import Autors
from rest_framework import status
from rest_framework.test import APITestCase


class AutorsAPITest(APITestCase):

    def setUp(self):
        self.author = Autors.objects.create(
            name="Test Author",
            bio="Test Bio",
            birth_date="2024-01-01"
        )

    def test_get_authors(self):
        response = self.client.get('/v1/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        data = {
            'name': 'New Author',
            'bio': 'New Bio',
            'birth_date': '2024-11-16'
        }
        response = self.client.post('/v1/authors/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieving_author(self):
        response = self.client.get(
            '/v1/authors/{}/'.format(self.author.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_author(self):
        data = {
            "name": "New Name Update",
            "bio": "New Bio Update",
            "birth_date": datetime.now().strftime('%Y-%m-%d')
        }
        response = self.client.put(
            '/v1/authors/{}/'.format(self.author.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify changes
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, "New Name Update")
        self.assertEqual(self.author.bio, "New Bio Update")
        self.assertEqual(str(self.author.birth_date),
                         datetime.now().strftime('%Y-%m-%d'))

    def test_deleting_author(self):
        response = self.client.delete(
            '/v1/authors/{}/'.format(self.author.id))

        # Assert the status code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Assert the object no longer exists
        self.assertFalse(Autors.objects.filter(id=self.author.id).exists())

    def test_retrieving_author_with_books(self):
        response = self.client.get(
            '/v1/authors/{}/books/'.format(self.author.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
