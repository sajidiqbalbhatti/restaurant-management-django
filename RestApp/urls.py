
from django.contrib import admin
from django.urls import path,include
from RestApp.views import*

urlpatterns = [
    path('',HomeView,name="home_cart"),
    path('about/',AboutView,name="about_page"),
    path('menu/',MenuView , name="menu_cart"),
    path('book/',BookTableView,name="book_table")

]
