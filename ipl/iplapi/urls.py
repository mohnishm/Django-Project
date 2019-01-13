from django.urls import path
from . import views

urlpatterns = [
    path('', views.matches_per_season, name='matches_ps'),
    path('winsperseason', views.wins_per_season, name='wins_ps'),
    path('extraruns', views.extra_runs, name='extra_runs'),
    path('economy', views.economy, name='economy'),
    path('batting_average', views.batting_average, name='batting_average')
]