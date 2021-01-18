from django.db import models

# Create your models here.

class Articles(models.Model):
    create_data = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField('Текст')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Статью'
        verbose_name_plural='Статьи'
