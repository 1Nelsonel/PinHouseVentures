from django.forms import ModelForm
from base.models import Comment,PropertyComment,MessageAgent
from django import forms


class CommentForm(ModelForm):
    class Meta:
        rating = forms.IntegerField(min_value=0, max_value=5, help_text="Max value is 5, min value is 0")

        model = Comment
        fields = ['name','email','rating','body']

class PropertyCommentForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    rating = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter rating between 0 to 5'}))

    class Meta:
        model = PropertyComment
        fields = ['name','email','rating','body']

class MessageAgentForm(ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
   

    class Meta:
        model = MessageAgent
        fields = ['full_name','email','phone_number','body']