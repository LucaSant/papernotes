from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Task

# Create your views here.
def index(request):

    posts = Post.objects.all()
    return render(request, 'papers/index.html', {'posts': posts})

def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)

    return render(request, 'papers/post_details.html', {'post':post})

def create_post(request):
    if request.method == 'POST':
        title = request.POST['post_name']
        color = request.POST['color_input']
        Post.objects.create(post_title=title, color=color).save()
        return redirect('/')
    else:
        return render(request, 'papers/create_post.html')
