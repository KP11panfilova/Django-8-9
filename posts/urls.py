from django.urls import path
from posts.views import *
from . import views
from django.contrib import admin
from django.urls import path, include
from .views import PostListView, PostDetailView
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404

#handler404 = 'posts.views.handler404'
urlpatterns = [
    path('', index),
    path('auth/', authorization),
    #path('admin/', admin.site.urls),
    #path('posts/', include('posts.urls')),
    path('', PostListView.as_view(), name='post_list'),
    #path('', views.post_list, name='post_list'),
    #path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', create_post, name='create_post'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]