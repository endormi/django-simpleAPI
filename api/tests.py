from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


class MovieTests(APITestCase):
    def test_movie_url(self):
        """
        Ensure we can get an object.
        """
        url = ('/movies/')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_movies_url_post(self):
        """
        Ensure we can create a new object.
        """
        data = {"name": "The Shining", "description": "A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence, while his psychic son sees horrific forebodings from both past and future.", "category": "Drama, Horror", "director": "Stanley Kubrick", "based_on": "Stephen King's novel", "main_actor": "Jack Nicholson", "release_date": "1980-06-13T00:00:00Z"}
        url = ('/movies/')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
