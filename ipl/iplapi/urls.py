from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path('matchesps', views.matches_per_season_charts, name='matches_ps'),
    path('winsperseason', views.wins_per_season_charts, name='wins_ps'),
    path('extraruns', views.extra_runs_charts, name='extra_runs'),
    path('economy', views.economy_charts, name='economy'),
    path('batting_average', views.batting_average_charts, name='batting_avg'),
    path("json/matchesps/", views.matches_per_season, name="total_matches"),
    path("json/winsperseason/", views.wins_per_season, name="wins_of_teams"),
    path("json/extraruns/", views.extra_runs, name="extra_runs"),
    path("json/economy/", views.economy, name="top_bowlers"),
    path("json/batting_average/", views.batting_average, name="batting_average"),  

]