from django.forms import ModelForm, TextInput
from .models import Comment, Post


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message': TextInput(attrs={'class': 'form-control'})
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['headline', 'body']

    def customSave(self, user):
        lv = self.save(commit=False)
        lv.created_by = user
        lv.save()
        return lv
