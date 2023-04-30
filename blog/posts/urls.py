from django.urls import path

from . import views

urlpatterns = [
    path('article/', views.articleView, name='articleView'),
    path('newPost/', views.newPostView, name='newPostView'),
    path('editPost/', views.editPostView, name='editPostView'),
    
    
    
    path('api/newPost/', views.newPost, name='newPost'),
    path('api/editPost/', views.editPost, name='editPost'),
    path('api/deletePost/', views.deletePost, name='deletePost'),
]