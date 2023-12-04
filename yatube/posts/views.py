from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('все посты')

def group_posts(request,pk):
  return HttpResponse(f'пост номер {pk}')
