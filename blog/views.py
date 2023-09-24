from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm
from .models import Post

def flontpage(request):
    posts = Post.objects.all()
    print('dskjhgsdku', posts.count())
    return render(request, 'blog/flontpage.html', {"posts": posts})  

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    form = CommentForm() 
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_detail",slug=post.slug)
        else:
            form = CommentForm()
          
    return render(request, 'blog/post_detail.html', {"post": post, "form": form})

from django.shortcuts import render, redirect
from .forms import PostForm

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
