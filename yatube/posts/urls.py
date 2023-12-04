from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>',views.group_posts),
    path('',views.index)
] 