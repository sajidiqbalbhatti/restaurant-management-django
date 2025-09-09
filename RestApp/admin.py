from django.contrib import admin
from .models import  *
from django.utils.text import Truncator

# Register your models heBooking_date')


class bAdmin(admin.ModelAdmin):
    list_display = ('Name','Phone_number','Email','No_person','booking_date')
    
class itemAdmin(admin.ModelAdmin):
    list_display=('Item_name','description','price','category','image')
    
admin.site.register(Category)
admin.site.register(Item,itemAdmin)
admin.site.register(AboutUs)
admin.site.register(BookTable,bAdmin)
