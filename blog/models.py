from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Note(models.Model):

    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    message = models.TextField(default='', verbose_name=_('Текст статьи'))
    public = models.BooleanField(default=False, verbose_name=_('Опубликовать'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Время создания'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Время обновления'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Автор'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('запись')
        verbose_name_plural = _('записи')


class Comment(models.Model):
    class Ratings(models.IntegerChoices):
        WITHOUT_RATING = 0, _('Без оценки')
        TERRIBLE = 1, _('Ужасно')
        BADLY = 2, _('Плохо')
        FINE = 3, _('Нормально')
        GOOD = 4, _('Хорошо')
        EXCELLENT = 5, _('Отлично')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name=_('comments'))
    rating = models.IntegerField(default=Ratings.WITHOUT_RATING, choices=Ratings.choices, verbose_name=_('Оценка'))

    def __str__(self):
        return f'{self.get_rating_display()}: {self.author}'

    class Meta:
        verbose_name = _('комментарий')
        verbose_name_plural = _('комментарии')
