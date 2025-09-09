from django.test import TestCase
from .forms import *
#
# Create your tests here.

class TestForm(TestCase):
    
    def test_form_valid_data(self):
        
        form_data = {
            'name': 'sajid',
            'email': '@example.com',
        }
        
        form = GeeksForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

