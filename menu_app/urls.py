from . import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    re_path(r'^(?P<path>.*)/$', views.CustomPage.as_view(), name='page'),
]