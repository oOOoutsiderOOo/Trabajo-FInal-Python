from django.urls import path

from . import views

urlpatterns = [

    path('api/newComment/', views.createComment, name='createComment'),
]