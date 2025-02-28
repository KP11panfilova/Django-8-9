from django.contrib import admin
from .models import Books, Chapter

class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published')
    list_filter = ('is_published',)
    inlines = [ChapterInline]
    readonly_fields = ('publication_date',)

    actions = ['unpublish_books']

    def unpublish_books(self, request, queryset):
        queryset.update(is_published=False)
    unpublish_books.short_description = "Снять с публикации"

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'book')
    search_fields = ('title', 'book__title')

# Register your models here.
