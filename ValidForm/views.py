from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import GeeksModel
from .forms import GeeksForm

# Create your views here.
def geeks_create(request):
    if request.method == 'POST':
        form = GeeksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('geeks_list')
    else:
        form = GeeksModel()
    return render(request, 'geeks_form.html', {'form': form})
    