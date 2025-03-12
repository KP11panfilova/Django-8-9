from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/', include('reviews.urls')),
]
urlpatterns = [
    path('add/', views.add_book, name='add_book'),
]