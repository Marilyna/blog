from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

from blog.models import Post


def index(request):
    all_posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'index.html', {'all_posts': all_posts})

# @login_required(redirect_field_name='login_view')

def post(request, post_id):
    pass