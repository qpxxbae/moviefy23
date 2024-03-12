from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def home_page(request):
    posts = Post.objects.all()[:4]
    return render(request,"./index.html",{'posts':posts})

def news_page(request):
    posts = Post.objects.all()
    return render(request,"./news.html",{'posts':posts} )

def news_detail_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,"./news_detail.html",{'post':post} )

def about_page(request):
    return render(request,'./about.html')