from datetime import datetime

from main.models import Autors, Books
from rest_framework import status
from rest_framework.test import APITestCase


class BooksAPITest(APITestCase):

    def setUp(self):

        self.authors = Autors.objects.create(
            name="Test Author",
            bio="Test Description",
            birth_date="2024-01-01"
        )

        self.book = Books.objects.create(
            title="Test Books",
            description="Test Description",
            publish_date="2024-01-01",
            author_id=self.authors,
        )

    def test_get_books(self):
        response = self.client.get('/v1/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        data = {
            'title': 'New Books',
            'description': 'New Description',
            'publish_date': '2024-11-16'
        }
        response = self.client.post('/v1/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieving_book(self):
        response = self.client.get(
            '/v1/books/{}/'.format(self.book.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        data = {
            "title": "New Title Update",
            "description": "New Description Update",
            "publish_date": datetime.now().strftime('%Y-%m-%d')
        }
        response = self.client.put(
            '/v1/books/{}/'.format(self.book.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify changes
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "New Title Update")
        self.assertEqual(self.book.description, "New Description Update")
        self.assertEqual(str(self.book.publish_date),
                         datetime.now().strftime('%Y-%m-%d'))

    def test_deleting_book(self):
        response = self.client.delete(
            '/v1/books/{}/'.format(self.book.id))

        # Assert the status code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Assert the object no longer exists
        self.assertFalse(Books.objects.filter(id=self.book.id).exists())
