from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home(request):
    return render(request, 'home.html')

# With signup view, the user could create an account in the system. 
# We uses the POST method to send the info
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            #there is the form that the template receive
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #With the create_user method we create the user
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save() #With save, we create in the table that django has preload
                login(request, user) #Create a cookie with the person account
                return redirect('tasks')
            #If an error exists, we send the error to the template, and the template show it
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        #If password does not match, we send the error
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })

#we logout with the logout function that django has
def signout(request):
    logout(request)
    return redirect('home')


def tasks(request):
    return render(request, 'tasks.html')

# With signin view, the user could login to an account that allready exists. 
# We uses the POST method to send the info
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm #form that the template receives
        })
    else:
        #The view receives the user and passs from the template
        username = request.POST['username']
        password = request.POST['password']
        #authenticate function validates if there is an account with that user and pass in the DB
        user = authenticate(request, username=username, password=password) 

        #If does not exist or is incorrect, throw an error
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'User or pass incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')
