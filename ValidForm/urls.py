from django.contrib import admin
from django.urls import path,include
from ValidForm.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',geeks_create, name='geeks_list')
    
    
]
