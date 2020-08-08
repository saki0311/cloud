from django.urls import path
from . import views

app_name='rikumane_app'

urlpatterns = [
<<<<<<< HEAD
    path('index', views.index, name='index'),
    path('ivents', views.ivents, name='ivents'),
=======
    path("", views.index, name='index'),
>>>>>>> 9afd29d9bb78d4740baf983ad404f27500b98302
]