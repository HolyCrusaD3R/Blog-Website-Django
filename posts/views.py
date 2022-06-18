from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post, Comment


def posts(request, page):
    posts_len = Post.objects.count()
    post_arr = Post.objects.order_by("-updated")[(page - 1) * 10:(page * 10)]
    if posts_len % 10 == 0:
        all_page_num = posts_len // 10
    else:
        all_page_num = (posts_len // 10) + 1
    context = {
        "posts": post_arr,
        "next_page": page+1,
        "previous_page": page-1,
        "all_page_num": all_page_num
    }
    return render(request, 'posts/posts.html', context)


def post(request, pk):
    post_object = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post_object)
    context = {
        "post": post_object,
        "comments": comments
    }
    return render(request, 'posts/post.html', context)
