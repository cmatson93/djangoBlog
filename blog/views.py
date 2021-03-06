from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug = slug)
    return render(request, 'blog/post_details.html', {'post': post})

def about_page(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')
