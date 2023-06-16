
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from decouple import config
from .forms import FiltersForm, VulnerabilityForm, DescriptionForm, MetricForm
from .models import Vulnerability
from django.db.models import  Q


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

@login_required
def vulnerabilities(request):
    if request.method == 'GET':
         print(request.GET)
         if 'state' in request.GET and request.GET['state'] == 'Fixeada':
              severity = request.GET.get('severity')
              if severity and severity != 'ALL':
               vulnerabilities = Vulnerability.objects.filter(Q(metrics__base_severity=severity) | Q(metrics__isnull=True)).prefetch_related('descriptions', 'metrics').order_by('-last_modified')
               return render(request, 'vulnerabilities.html', {'vulnerabilities':vulnerabilities, 'form': FiltersForm})           
              else:
               vulnerabilities = Vulnerability.objects.all().prefetch_related('descriptions', 'metrics')
               return render(request, 'vulnerabilities.html', {'vulnerabilities':vulnerabilities, 'form': FiltersForm})
         else:
            api_vulnerabilities = config('API_VULNERABILITIES')
            try:
               response = requests.get(api_vulnerabilities)
               severity = request.GET.get('severity')
               vulnerabilities_database = Vulnerability.objects.all().prefetch_related('descriptions', 'metrics')
               if severity and severity != 'ALL':
                   params = {'cvssV2Severity': request.GET.get('severity')}
                   response =  requests.get(api_vulnerabilities, params=params)
                   vulnerabilities_database = Vulnerability.objects.filter(Q(metrics__base_severity=severity) | Q(metrics__isnull=True)).prefetch_related('descriptions', 'metrics').order_by('-last_modified')
               if response.status_code == 200:
                   data = response.json()
                   vulnerabilities_database_List = list(vulnerabilities_database)
                   vulnerabilities_all = vulnerabilities_database_List + data['vulnerabilities']
                   return render(request, 'vulnerabilities.html', {'vulnerabilities': vulnerabilities_all, 'form': FiltersForm})
               else:
                   return render(request, 'vulnerabilities.html', {'error': 'Error en la solicitud'})
            except requests.exceptions.RequestException as e:
                return render(request, 'vulnerabilities.html', {'error': str(e)})
         
@login_required   
def register_vulnerabilities(request):
     if request.method == 'POST':
       try:
            form = VulnerabilityForm(request.POST)
            if form.is_valid():
             vulnerability = form.save() 
             description_form = DescriptionForm(request.POST)
             if description_form.is_valid():
                description = description_form.save(commit=False)
                description.vulnerability = vulnerability  
                description.save() 
                severity = MetricForm(request.POST)
                if severity.is_valid():
                    severity = severity.save(commit=False)
                    severity.vulnerability = vulnerability  
                    severity.save() 
                    return redirect('vulnerabilities',)
       except ValueError:
            return render(request, 'create_task.html', {"form": VulnerabilityForm, "error": "Error creating task."})

     else:   
       return render(request, 'create_vulnerability.html', {'form': VulnerabilityForm, 'description_form': DescriptionForm, 'severity':MetricForm})
     

@login_required
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



