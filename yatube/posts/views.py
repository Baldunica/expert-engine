from django.shortcuts import render,get_object_or_404
from .models import Post,Group

def index(request):
  template = 'posts/index.html'
  posts = Post.objects.order_by('-pub_date')[:10]
  context = {
    'title': 'Последние обновления на сайте',
    'posts':posts,
  }
  return render(request,template,context)

def group_posts(request,slug):
  template = 'posts/group_list.html'
  group = get_object_or_404(Group,slug = slug)
  posts = Post.objects.filter(group = group).order_by('-pub_date')
  context = {
    'title': f'Записи сообщества с {slug} цитатами',
    'posts':posts,
    'slug': slug,
  }
  return render(request,template,context)

def lev_tolstoy(request):
  template = 'posts/leva.html'
  title = 'Lev tOlstoy'
  context = {
    'title': title,
    'text': 'Infa pro tOlstogo',
  }
  return render(request,template,context)