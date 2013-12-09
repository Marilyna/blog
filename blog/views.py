from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from blog.models import Post
from blog.forms import LoginForm


def index(request):
    all_posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'index.html', {'all_posts': all_posts})


@login_required(redirect_field_name='sign_in')
def edit_post(request, post_id):
    pass


def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect(index)
    else:
        form = LoginForm()
    return render(request, 'login.html',
                  {'form': form})


@login_required(redirect_field_name='sign_in')
def sign_out(request):
    logout(request)
    return redirect(index)