from django.shortcuts import render, redirect
from django.contrib.auth.models import User        
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'registration/signup.html', {'form':form})