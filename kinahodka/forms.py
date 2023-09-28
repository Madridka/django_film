from django import forms
from .models import Rating, Comment


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')