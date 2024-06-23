from django.urls import path
from .api import anime_list

urlpatterns = [
    path('animes',anime_list,name='animelist')
]
