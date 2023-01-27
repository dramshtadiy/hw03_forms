from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {
            'text': ('Текст поста'),
            'group': ('Группа'),
        }
        new_texts = {
            'text': ('Напишите красивый пост'),
            'group': ('Выберите группу'),
        }

    def clean_text(self):
        data = self.cleaned_data['text']
        if '' not in data:
            raise forms.ValidationError('Не может быть пустым!')
        return data
