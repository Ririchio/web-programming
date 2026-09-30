from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title} — {self.author}'