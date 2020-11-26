from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='rikumane_app'

urlpatterns = [
    path('', views.login, name='top'),
    path('detail/',views.detail,name='detail'),
    path('index/', views.index, name='index'),
    path('calendar/', views.calendar, name='calendar'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
]
