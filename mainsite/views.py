from django.shortcuts import render, redirect
#from django.http import HttpResponse
from datetime import datetime
from .models import Post


def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    #print(posts)
    return render(request, 'index.html', locals())


def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())

    except:
        return redirect('/')