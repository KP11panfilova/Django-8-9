from django.contrib import admin
from posts.models import *
from .models import  Author, Genre, Book

admin.site.register(Tag)
admin.site.register(Post)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'is_available')
    list_filter = ('genre', 'is_checked_out')
    search_fields = ('title', 'author__name')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
# Register your models here.
