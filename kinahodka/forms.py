from django import forms
from .models import Comment

"""форма для комментариев и оценки от пользователя."""
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment', 'rating')
