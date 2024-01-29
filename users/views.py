from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(req):
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account has been created.👍')
            return redirect('store-index')
    else:
        form = UserRegistrationForm()

    return render(req, 'users/register.html', {"form" : form})

@login_required
def profile(req):
    return render(req, 'users/profile.html')