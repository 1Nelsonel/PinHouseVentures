from django.forms import ModelForm
from base.models import Comment
from django import forms


class CommentForm(ModelForm):
    class Meta:
        rating = forms.IntegerField(min_value=0, max_value=5, help_text="Max value is 5, min value is 0")

        model = Comment
        fields = ['name','email','rating','body']