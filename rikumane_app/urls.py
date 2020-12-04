from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='rikumane_app'

urlpatterns = [
    path('', views.login, name='top'),
    path('detail/',views.detail,name='detail'),
    path('index/', views.index, name='index'),
    path('calendar/', views.calendar, name='calendar'),
]
