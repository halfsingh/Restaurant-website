from django import forms
from django.forms import fields
from .models import Comment

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        