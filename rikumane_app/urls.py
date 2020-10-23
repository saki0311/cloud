from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='rikumane_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/',views.detail,name='detail'),
    path('login/', views.login, name='login'),
    path('logout/', views.login, name='logout'),
]
