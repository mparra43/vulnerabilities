
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from decouple import config

from .forms import FiltersForm, VulnerabilityForm, DescriptionForm


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        print( UserCreationForm)
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('vulnerabilities')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})


def vulnerabilities(request):
    if request.method == 'GET':
         if 'state' in request.GET and request.GET['state'] == 'Fixeadas':
             return render(request, 'vulnerabilities.html', {'form': FiltersForm})
         else:
            api_vulnerabilities = config('API_VULNERABILITIES')
            try:
               response = requests.get(api_vulnerabilities)
               severity = request.GET.get('severity')
               if severity and severity != 'ALL':
                   params = {'cvssV2Severity': request.GET.get('severity')}
                   response =  requests.get(api_vulnerabilities, params=params)
               if response.status_code == 200:
                   data = response.json()
                   return render(request, 'vulnerabilities.html', {'vulnerabilities': data['vulnerabilities'], 'form': FiltersForm})
               else:
                   return render(request, 'vulnerabilities.html', {'error': 'Error en la solicitud'})
            except requests.exceptions.RequestException as e:
                return render(request, 'vulnerabilities.html', {'error': str(e)})
         
    
def register_vulnerabilities(request):
    return render(request, 'create_vulnerability.html', {'form': VulnerabilityForm})
        

def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('vulnerabilities')


def create_vulnerability(request):
    if request.method == 'POST':
        form = VulnerabilityForm(request.POST)
        if form.is_valid():
            vulnerability = form.save() 
            description_form = DescriptionForm(request.POST)
            if description_form.is_valid():
                description = description_form.save(commit=False)
                description.vulnerability = vulnerability  
                description.save()  
            return redirect('vulnerability_detail', pk=vulnerability.pk)
    else:
        form = VulnerabilityForm()
        description_form = DescriptionForm()
    return render(request, 'create_vulnerability.html', {'form': form, 'description_form': description_form})
