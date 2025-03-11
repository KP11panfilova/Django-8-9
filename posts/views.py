from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from posts.models import *
from .models import Post
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {'posts':posts, 'title':"Hello isip28!"})

def authorization(request):
    return HttpResponse("<h1>Authorization</h1>")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})
    
def handler404(request, exception):
    return render(request, '404.html', status=404)