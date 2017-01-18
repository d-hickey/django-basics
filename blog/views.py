from django.shortcuts import render

from blog.models import Post

# Create your views here.
def index(request):
    recent = Post.objects.order_by('-pub_date')[:10]
    return render(request, "blog/index.html", {'recent': recent})

def user(request, user):
    return index(request)

def post(request, user, post_id):
    return index(request)
