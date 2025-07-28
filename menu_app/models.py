from django.db import models


class Menu(models.Model):
    """Модель для построения меню"""
    title = models.CharField(verbose_name='Название меню', max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Список меню'


class MenuItem(models.Model):
    """Модель для отдельных пунктов меню с ссылками и названиями"""
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Меню', related_name='items')
    title = models.CharField(verbose_name='Название ссылки', max_length=100)
    url = models.CharField(verbose_name='Адрес ссылки', max_length=200, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Родительский класс', null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'