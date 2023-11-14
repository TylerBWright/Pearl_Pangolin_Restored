from django.urls import path, include
from django.contrib import admin
from pp.views import (
    about,
    index,
    play,
    submit_animal
)

app_name = 'pp'

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('about/', about, name='about'),
    path('play/', play, name='play'),
    path("submit/", submit_animal, name="submit_animal"),
]
