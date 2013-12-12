from datetime import datetime
from blog.models import Post

from django import forms
from django.contrib.auth import authenticate

from multifilefield.forms import MultiFileField


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'),
                            password=self.cleaned_data.get('password'))
        if user is None:
            raise forms.ValidationError("Wrong login or password")
        if not user.is_active:
            raise forms.ValidationError("Your account is disabled")
        self.user = user
        return self.cleaned_data


class CreatePostForm(forms.Form):
    # class Meta:
    #     model = Post
    #     fields = ('title', 'content', 'images')
    #     widgets = {
    #         'content': forms.Textarea(attrs={'rows': 10})
    #     }
    title = forms.CharField(max_length=200, required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10}))
    files = MultiFileField(required=False)
    simple = forms.ImageField(required=False)