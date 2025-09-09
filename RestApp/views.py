from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def HomeView(request):
    It=Item.objects.all()
    cat = Category.objects.all()
    return render(request,'index.html',{'cat':cat,'It':It})
def AboutView(request):
    data = AboutUs.objects.all()
    return render (request,'about.html',{'data' : data})
def MenuView(request):
    It=Item.objects.all()
    cat = Category.objects.all()
    
    return render(request, 'menu.html',{'cat':cat,'It':It})
def BookTableView(request):
    data = None 
    if request.method=='POST':
        name= request.POST.get('name')
        phone= request.POST.get('phone')
        email= request.POST.get('email')
        total_P= request.POST.get('no_person')
        bookingDate= request.POST.get('date')
        
        data=BookTable.objects.create(
            Name=name,
            Phone_number=phone,
            No_person=total_P,
            booking_date=bookingDate,
            Email=email
            
        )
        return redirect('/book/')
    return render(request,'book.html',{'data':data})
