from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Category,Tag


def index(request):
    return render(request, 'blog/index.html')


def get_category(request,slug):
    return render(request, 'blog/category.html')
