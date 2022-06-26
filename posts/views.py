from django.shortcuts import render, redirect, reverse
from .models import Post, Comment
from .forms import CommentForm, PostForm


def posts(request, page):
    posts_len = Post.objects.count()
    post_arr = Post.objects.order_by("-updated")[(page - 1) * 10:(page * 10)]
    if posts_len % 10 == 0:
        all_page_num = posts_len // 10
    else:
        all_page_num = (posts_len // 10) + 1
    context = {
        "posts": post_arr,
        "next_page": page + 1,
        "previous_page": page - 1,
        "all_page_num": all_page_num
    }
    return render(request, 'posts/posts.html', context)


def post(request, pk):
    form = CommentForm()
    post_object = Post.objects.get(id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        form.instance.user = request.user
        form.instance.post = post_object
        if form.is_valid():
            form.save()
            return redirect('post', pk=pk)
    comments = Comment.objects.filter(post=post_object)
    context = {
        "post": post_object,
        "comments": comments,
        "form": form
    }
    return render(request, 'posts/post.html', context)


def blog(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            curr = form.customSave(form.instance.user)
            return redirect('post', pk=curr.id)
    context = {
        "form": form
    }
    return render(request, 'posts/blog.html', context)
