from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
import pdb


def main(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/main.html', context)


def new(request):
    context = {
        'form': PostForm()
    }
    return render(request, 'posts/new.html', context)


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main')
    
    
def show(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/show.html', context)


def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post,
        'form': PostForm(instance=post)
    }
    return render(request, 'posts/edit.html', context)


def update(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(pk=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts:show', post_id)
    
        
        
        
        