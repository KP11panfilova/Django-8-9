from django.db import models
class Books(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    publication_date = models.DateField(verbose_name="Дата публикации", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Chapter(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="chapters", verbose_name="Книга")
    title = models.CharField(max_length=200, verbose_name="Название главы")
    content = models.TextField(verbose_name="Содержание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Глава"
        verbose_name_plural = "Главы"

