from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    """Главная и изначальная страница в приложении"""
    template_name = 'menu_app/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomPage(TemplateView):
    """Кастомная страница при переходе по ссылкам"""
    template_name = 'menu_app/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context