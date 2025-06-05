from django.urls import path
from . import views

app_name = 'player'

urlpatterns = [
    path('', views.index, name='index'),
    path('play-pause/', views.play_pause, name='play_pause'),
    path('stop/', views.stop, name='stop'),
    path('next/', views.next_track, name='next'),
    path('previous/', views.previous, name='previous'),
    path('volume-up/', views.volume_up, name='volume_up'),
    path('volume-down/', views.volume_down, name='volume_down'),
    path('mute/', views.mute, name='mute'),
]