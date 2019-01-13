from django.urls import path
from . import json_views, template_views

urlpatterns = [
    path("", template_views.Home, name="home"),
    path('matchesps', template_views.matches_per_season, name='matches_ps'),
    path('winsperseason', template_views.wins_per_season, name='wins_ps'),
    path('extraruns', template_views.extra_runs, name='extra_runs'),
    path('economy', template_views.economy, name='economy'),
    path('batting_average', template_views.batting_avg, name='batting_avg'),
    path("json/matchesps/", json_views.matches_per_season, name="total_matches"),
    path("json/winsperseason/", json_views.wins_per_season, name="wins_of_teams"),
    path("json/extraruns/", json_views.extra_runs, name="extra_runs"),
    path("json/economy/", json_views.economy, name="top_bowlers"),
    path("json/batting_average/", json_views.batting_avg, name="batting_average"),  

]