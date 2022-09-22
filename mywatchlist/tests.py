from django.test import TestCase, Client
from django.urls import reverse
from mywatchlist.models import MyWatchlist

# Create your tests here.

class TestViews(TestCase):
    def test_project_list_HTML(self):
        self.client = Client()
        response = self.client.get(reverse('mywatchlist:show_watchlist'))
        
        self.assertEquals(response.status_code, 200)
        
    def test_project_list_XML(self):
        self.client = Client()
        response = self.client.get(reverse('mywatchlist:show_xml'))
        
        self.assertEquals(response.status_code, 200)
        
    def test_project_list_JSON(self):
        self.client = Client()
        response = self.client.get(reverse('mywatchlist:show_json'))
        
        self.assertEquals(response.status_code, 200)