from django.urls import path, include
from django.contrib import admin
from pp.views import (
    about,
    index,
    play
)

app_name = 'pp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('play/', play, name='play'),
]
