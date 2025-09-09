from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    Item_name = models.CharField(max_length=15)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category= models.ForeignKey(Category,related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Item/')
    
    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)
    def __str__(self):
        truncated_description = ' '.join(self.Description.split()[:10])
        # Add ellipsis if the original description is longer than 30 words
        if len(self.Description.split()) > 10:
            truncated_description += '........'
        return truncated_description
     
        

class BookTable(models.Model):
    Name= models.CharField(max_length=100)
    Phone_number=models.IntegerField()
    Email = models.EmailField(max_length=200)
    No_person =models.IntegerField()
    booking_date =models.DateTimeField()
    
    def __str__(self):
        return self.Name
    
