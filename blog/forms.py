from django import forms
from django.contrib.auth import authenticate

from multifilefield.forms import MultiFileField

from blog.models import Post, Image


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
    title = forms.CharField(max_length=200, required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10}))
    files = MultiFileField(required=False)

    def clean(self):
        """
        Check if all files are images

        """
        if self.files:
            for file in self.files.getlist('files[]'):
                if not file.content_type.startswith('image/'):
                    raise forms.ValidationError("Only image files can be uploaded")
        return self.cleaned_data

    def save(self, author):
        post = Post(title=self.cleaned_data['title'].strip(),
                    content=self.cleaned_data['content'],
                    author=author)
        post.save()
        if self.files:
            for f in self.files.getlist('files[]'):
                im = Image(post=post)
                im.image.save(f.name, f)
        return post
