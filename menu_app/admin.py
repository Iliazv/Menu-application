from django.contrib import admin
from .models import (Menu, MenuItem)

# Логин/пароль для админа - admin (если используется готовая тестовая БД)

class MenuAdmin(admin.ModelAdmin):
    """Админ модель для меню"""
    fields = ['title']
    search_fields = ('title',)

class MenuFilter(admin.SimpleListFilter):
    """Кастомный фильтр для поиска пунктов меню по основному меню"""
    title = 'Menu'
    parameter_name = 'menu_filter'

    def lookups(self, request, model_admin):
        menus = set([m for m in model_admin.model.objects.values_list('menu__id', 'menu__title')])
        return [(m[0], m[1]) for m in menus]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(menu__id=self.value())
        return queryset

class MenuItemAdmin(admin.ModelAdmin):
    """Админ модель для пунктов меню"""
    fields = ['menu', 'title', 'url', 'parent']
    search_fields = ('title',)
    list_filter = (MenuFilter,)

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)