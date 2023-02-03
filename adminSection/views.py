from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from base.models import Property, Agent, Location, Propertycategory, Blog, Comment, Profile, User,PropertyComment
# ,MessageAgent
from django.contrib.auth.models import User
from django.forms import ModelForm

from .forms import PropertyForm,LocationForm,PropertycategoryForm


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    # counts
    property_count = Property.objects.all().count()
    review_count = PropertyComment.objects.all().count()
    # comments
    propertycomments = PropertyComment.objects.all()
    context = {'property_count': property_count,'review_count':review_count,'propertycomments':propertycomments}
    return render(request, 'adminSection/dashboard.html', context)
    

@login_required(login_url='login')
def addProperty(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.agent = request.user
            property.save()
            return redirect("my-property")
    else:
        form = PropertyForm()

    return render(request, 'adminSection/submit-property.html', {'form': form})

@login_required(login_url='login')
def addLocation(request):
    locations = Location.objects.all()
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save()
            location.save()
            return redirect("add-location")
    else:
        form = LocationForm()

    context = {'form': form, 'locations':locations}
    return render(request, 'adminSection/add-location.html', context)


@login_required(login_url='login')
def addPropertyCategory(request):
    categories = Propertycategory.objects.all()
    if request.method == 'POST':
        form = PropertycategoryForm(request.POST)
        if form.is_valid():
            productcategory = form.save()
            productcategory.save()
            return redirect("add-property-category")
    else:
        form = PropertycategoryForm()

    context = {'form': form, 'categories':categories}
    return render(request, 'adminSection/add-PropertyCategory.html', context)

@login_required(login_url='login')
def bookings(request):
    context = {}
    return render(request, 'adminSection/bookings.html', context)


@login_required(login_url='login')
def myProperty(request):
    properties = Property.objects.filter(agent=request.user)
    context = {'properties': properties}
    return render(request, 'adminSection/my-properties.html', context)

# ---------------------------------------------------------------------------


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = fields = ['username', 'email', 'first_name', 'last_name']


class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone_number', 'description']

# -----------------------------------------------------------------------------


@login_required(login_url='login')
@transaction.atomic
def myProfile(request):
    profiles = Profile.objects.all()

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()

            return redirect("my-profile")
    else:
        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.profile)

    context = {'user_form': user_form,
               'user_profile_form': user_profile_form, 'profiles': profiles}

    return render(request, 'adminSection/my-profile.html', context)


@login_required(login_url='login')
def messages(request):
    comments = MessageAgent.objects.filter(agent=request.user)
    context = {'comments':comments}
    return render(request, 'adminSection/messages.html', context)
