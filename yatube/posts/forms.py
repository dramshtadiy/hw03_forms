from django import forms
from .models import Post
from django.forms import Textarea


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {
            'text': ('Текст поста'),
            'group': ('Группа'),
        }
        help_texts = {
            'text': ('Напишите красивый пост'),
            'group': ('Выберите группу'),
        }
        widgets = {
            'text': Textarea,
        }
