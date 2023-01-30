from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from base.models import Property, Agent, Location, Propertycategory, Blog, Comment

# Create your views here.
# @login_required(login_url='login')
def dashboard(request):
    context = {}
    return render(request, 'adminSection/dashboard.html', context)

def addProperty(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'adminSection/submit-property.html', context)  

def bookings(request):
    context = {}
    return render(request, 'adminSection/bookings.html', context) 

def myProperty(request):
    properties = Property.objects.all()
    context = {'properties': properties}
    return render(request, 'adminSection/my-properties.html', context) 

def myProfile(request):
    context = {}
    return render(request, 'adminSection/my-profile.html', context) 

def messages(request):
    context = {}
    return render(request, 'adminSection/messages.html', context) 