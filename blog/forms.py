from django import forms

from blog.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class ComentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
