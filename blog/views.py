from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from blog.models import Post, Image, Category
from blog.forms import LoginForm, CreatePostForm


def index(request):
    all_posts = Post.objects.all().order_by('-published')
    context = {'posts': all_posts}
    context.update(_get_sidebar_context())
    return render(request, 'index.html', context)


def category_page(request, category_id):
    category = Category.objects.get(pk=category_id)
    context = {'posts': category.posts.order_by('-published')}
    context.update(_get_sidebar_context())
    return render(request, 'index.html', context)


def post_page(request, post_id):
    post = Post.objects.get(pk=post_id)
    images = Image.objects.filter(post=post)
    context = {'post': post, 'images': images}
    context.update(_get_sidebar_context())
    return render(request, 'post_page.html', context)


@login_required(login_url='sign_in')
def new_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(title=form['title'].data.strip(), content=form['content'].data, author=request.user)
            post.save()
            if form.files:
                for f in form.files.getlist('files[]'):
                    im = Image(post=post)
                    im.image.save(f.name, f)
            return redirect(index)
        else:
            form.files = {}
    else:
        form = CreatePostForm()

    context = {'form': form}
    return render(request, 'create_post.html', context)


def sign_in(request):
    nexturl = request.GET.get('next') or 'index'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect(request.POST.get('next'))
    else:
        form = LoginForm()

    context = {'form': form, 'next': nexturl}
    return render(request, 'login.html', context)


@login_required(login_url='sign_in')
def sign_out(request):
    logout(request)
    return redirect(index)


def _get_sidebar_context():
    all_categories = Category.objects.values('id', 'title')
    return {'categories': all_categories}
