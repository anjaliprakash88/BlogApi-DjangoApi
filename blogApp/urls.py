from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('get-all-post', views.getallposts),
    path('create-post', views.createpost),
    path('delete-post', views.deletepost),
    path('get-post', views.getpost),
    path('update-post', views.updatepost),
]
