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
        help_texts = forms.CharField(widget=forms.TextInput(attrs={
            'text': ('Напишите красивый пост'),
            'group': ('Выберите группу'),
        }))

    def clean_text(self):
        data = self.cleaned_data['text']
        return data
