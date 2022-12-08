from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ThingForm
from .models import Thing

def thing_view(request):
    form = ThingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('things')
    else:
        form = ThingForm()
    return render(request, 'thing.html',{'form':form})
