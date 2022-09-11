from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    obj = Post.objects.all()
    contex ={
        'obj':obj,
    }
    return render(request,'blog/index.html',contex)
