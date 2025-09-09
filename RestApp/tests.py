from django.test import TestCase
from django.urls import reverse , resolve
from RestApp.models import Category, Item
from .views import *
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.

class TestCase(TestCase):
    
    def setUp(self):
       self.category = Category.objects.create(name='Electronics')
       self.image = SimpleUploadedFile(name='test_image.jpg' , content=b'', content_type='image/jpeg')
    
    def test_create_item(self):
        
        item= Item.objects.create(
            Item_name='loptop',
            description='A powerful laptop',
            price=1000,
            category=self.category,
            image=self.image
        )
        self.assertEqual(item.Item_name,'loptop')
        self.assertEqual(item.description,'A powerful laptop')
        self.assertEqual(item.price, 1000)
        self.assertEqual(item.category, self.category)
        # self.assertEqual(item.image.name, 'Item/test_image.jpg')
        self.assertTrue(item.image.name.startswith('Item/test_image'))

class HomeView(TestCase):
    
    def setUp(self):
        
        self.category1 = Category.objects.create(name='Electronics')
        self.category2 = Category.objects.create(name='Clothing')
        
        
        self.item1 = Item.objects.create(
            Item_name='Samsung Galaxy S20',
            description='A powerful smartphone',
            price=1000,
            category=self.category1,
            image='path/to/image.jpg'
        ) 
        
        
        self.item2 = Item.objects.create(
            Item_name='Nike Air Max',
            description='A stylish shoe',
            price=50,
            category=self.category2,
            image='path/to/image.jpg'
        )
       
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home_cart'))
        self.assertEqual(response.status_code, 200)
        
        
    def test_home_view_template(self):
        response = self.client.get(reverse('home_cart'))
        self.assertTemplateUsed(response, 'index.html')
        
    def test_home_view_context(self):
        response = self.client.get(reverse('home_cart'))
        self.assertIn('It', response.context)
        self.assertIn('cat', response.context)
        
        self.assertEqual(list(response.context['It']), list(Item.objects.all()))
        self.assertEqual(list(response.context['cat']), list(Category.objects.all()))
        
    

class URLTests(TestCase):
    
    def test_home_url_resolves_to_home(self):
        
        url = reverse('home_cart')
        self.assertEqual(resolve(url) ,HomeView)
        
    
    
class URLTests(TestCase):

    def test_about_url_resolves_to_about_view(self):
        """Test if the '/about/' URL resolves to AboutView"""
        url = reverse('about_page')  # Generate the URL for 'about_page'
        self.assertEqual(resolve(url).func, AboutView)




