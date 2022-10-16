from django import forms

from blog_application.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_tag',
            'post_category',
            'post_header',
            'post_content',
        ]
        widgets = {

            'post_header': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input Header'}),
            'post_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Input Content'}),
        }
