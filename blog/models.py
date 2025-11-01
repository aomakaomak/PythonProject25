from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Опубликовано или нет')
    views_count = models.IntegerField(default=0)



    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'запись в блоге'
        verbose_name_plural = 'записи в блоге'
        ordering = ['title']

