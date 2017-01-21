from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect as redirect
from django.urls import reverse

from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    recent = Post.objects.order_by('-pub_date')[:10]
    return render(request, "blog/index.html", {'recent': recent})

def user(request, user):
    return index(request)

def post(request, user, post_id):
    return index(request)

def create (request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect(reverse('blog:post', args=(request.user.username, post.id,)))
    else:
        form = PostForm()
        return render(request, "blog/create.html", {'form': form})
