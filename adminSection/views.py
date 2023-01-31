from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from base.models import Property, Agent, Location, Propertycategory, Blog, Comment

# Create your views here.
# @login_required(login_url='login')

@login_required(login_url='login')
def dashboard(request):
    property_count = Property.objects.all().count()
    context = {'property_count': property_count}
    return render(request, 'adminSection/dashboard.html', context)

@login_required(login_url='login')
def addProperty(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'adminSection/submit-property.html', context)  

@login_required(login_url='login')
def bookings(request):
    context = {}
    return render(request, 'adminSection/bookings.html', context) 

@login_required(login_url='login')
def myProperty(request):
    properties = Property.objects.filter(agent=request.agent)
    context = {'properties': properties}
    return render(request, 'adminSection/my-properties.html', context) 

@login_required(login_url='login')
def myProfile(request):
    context = {}
    return render(request, 'adminSection/my-profile.html', context) 

@login_required(login_url='login')
def messages(request):
    context = {}
    return render(request, 'adminSection/messages.html', context) 