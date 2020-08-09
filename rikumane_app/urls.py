from django.urls import path
from . import views

app_name='rikumane_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('ivents/', views.ivents, name='ivents'),
    path('add_event/',views.add_event,name='add_event'),
]