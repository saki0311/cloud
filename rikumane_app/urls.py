from django.urls import path
from . import views

app_name='rikumane_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/',views.detail,name='detail'),
]