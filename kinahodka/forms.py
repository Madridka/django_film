from django import forms
from .models import *


"""форма для комментариев и оценки от пользователя."""
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment', 'rating')


class AddFilm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'url_kp': forms.TextInput(attrs={"size": "40"})
        }
