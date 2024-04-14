from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coin', views.coin, name='coin'),
    path('cube', views.cube, name='cube'),
    path('random', views.random_number, name='random_number'),
    path('game', views.game, name='game'),
    path('stats', views.stats, name='stats'),
    path('author', views.create_author, name='author')
]