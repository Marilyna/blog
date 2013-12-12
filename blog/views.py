from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from blog.models import Post, Image
from blog.forms import LoginForm, CreatePostForm


def index(request):
    all_posts = Post.objects.all().order_by('-published')
    return render(request, 'index.html', {'all_posts': all_posts})


@login_required(login_url='sign_in')
def post_page(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post_page.html', {'post': post})


@login_required(login_url='sign_in')
def new_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(title=form['title'].data, content=form['content'].data, author=request.user)
            post.save()
            import pdb; pdb.set_trace()
            image = Image(post=post)
            image.image.save(form.files['simple'].name, form.files['simple'])

            return redirect(index)
    else:
        form = CreatePostForm()
        return render(request, 'create_post.html', {'form': form})


def sign_in(request):
    nexturl = request.GET.get('next') or 'index'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect(request.POST.get('next'))
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'next': nexturl})


@login_required(login_url='sign_in')
def sign_out(request):
    logout(request)
    return redirect(index)