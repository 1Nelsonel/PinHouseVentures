from django.forms import ModelForm
from base.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name']