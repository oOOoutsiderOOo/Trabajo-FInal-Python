from django.urls import path

from . import views

urlpatterns = [
    path('newPost/', views.newPostView, name='newPostView'),
    
    
    path('api/newPost/', views.newPost, name='newPost'),
]