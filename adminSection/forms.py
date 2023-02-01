from django.forms import ModelForm
from base.models import User,Profile,Property,Location,Propertycategory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = fields = ['username', 'email','first_name', 'last_name']

class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image','phone_number','description']

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class PropertycategoryForm(ModelForm):
    class Meta:
        model = Propertycategory
        fields = '__all__'