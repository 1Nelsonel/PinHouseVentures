from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from base.models import Property, Agent, Location, Propertycategory, Blog, Comment, Profile, User
from django.contrib.auth.models import User
from django.forms import ModelForm

from .forms import PropertyForm


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    property_count = Property.objects.all().count()
    context = {'property_count': property_count}
    return render(request, 'adminSection/dashboard.html', context)


@login_required(login_url='login')
# def addProperty(request):
#     if request.method == 'POST':
#         form = PropertyForm(request.POST, request.FILES)
#         if form.is_valid():
#             property = form.save(commit=False)
#             if 'imageOne' in request.FILES:
#                 property.imageOne = request.FILES['imageOne']
#             if 'imageTwo' in request.FILES:
#                 property.imageTwo = request.FILES['imageTwo']
#             if 'imageThree' in request.FILES:
#                 property.imageThree = request.FILES['imageThree']
#             if 'imageFour' in request.FILES:
#                 property.imageFour = request.FILES['imageFour']
#             if 'imageFive' in request.FILES:
#                 property.imageFive = request.FILES['imageFive']
#             property.save()
#             return redirect("my-property")
#     else:
#         form = PropertyForm()
#     context = {'form': form}
#     return render(request, 'adminSection/submit-property.html', context)
def addProperty(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("my-property")
    else:
        form = PropertyForm()

    return render(request, 'adminSection/submit-property.html', {'form': form})


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
# def myProfile(request):
#     profiles = Profile.objects.all()

#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         user_profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if user_form.is_valid() and user_profile_form.is_valid():
#             user_form.save()
#             user_profile_form.save()

#             return redirect("my-profile")

#     else:
#         user_form = UserForm(instance=request.user)
#         user_profile_form = UserProfileForm(instance=request.user.profile)

#     context = {'user_form': user_form,
#                'user_profile_form': user_profile_form, 'profiles': profiles}

#     return render(request, 'adminSection/my-profile.html', context)

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
    context = {}
    return render(request, 'adminSection/messages.html', context)
