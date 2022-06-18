from django.forms import ModelForm, TextInput
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message': TextInput(attrs={'class': 'form-control'})
        }
