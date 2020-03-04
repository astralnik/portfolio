from django.db import models
from django.utils import timezone

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:         # Перевод для админки
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'


class Comment(models.Model):
    title = models.ForeignKey(Note, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:         # Перевод для админки
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
