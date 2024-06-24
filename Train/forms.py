# forms.py
from django import forms
from .models import Station,Train,Comment

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Station
        fields='__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model=Train
        fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']