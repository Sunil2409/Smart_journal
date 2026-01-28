from django.test import TestCase
from django.urls import reverse

class SmartJournalTests(TestCase):
    def test_homepage_status_code(self):
        # This checks if the home page loads (HTTP 200)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)