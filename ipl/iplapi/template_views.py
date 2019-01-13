from django.http import HttpResponse
from django.shortcuts import render
import json
from .data import DataFromDb


queried_data = DataFromDb()


def Home(request):
    return render(request, "iplapi/home.html")


def matches_per_season(request):
    matches_data = queried_data.matches_per_season()
    data = {
        "matches_data":dict(matches_data),
        "title":"Matches Per Season",
        "text":"Number of Matches",
        "bottom":"Seasons"
    }
    json_data = json.dumps(data)
    return render(request, "iplapi/matches.html", context={"data":json_data})

def wins_per_season(request):
    matches_data = queried_data.wins_per_season()
    data = {
        "matches_data":dict(matches_data),
        "title":"Wins per team for every season ",
        "text":"Number of wins",
        "bottom":"Seasons"
    }
    json_data = json.dumps(data)
    return render(request, "iplapi/winsperseason.html", context={"data":json_data})

def extra_runs(request):
    matches_data = queried_data.extra_runs()
    data = {
        "matches_data":dict(matches_data),
        "title":"Extra runs conceded by each team in 2016",
        "text":"Extra runs",
        "bottom":"teams"
    }
    json_data = json.dumps(data)
    return render(request, "iplapi/extraruns.html", context={"data":json_data})


def economy(request):
    matches_data = queried_data.economy()
    data = {
        "matches_data":dict(matches_data),
        "title":"Top economical bowlers of 2015",
        "text":"Economy",
        "bottom":"Bowlers"
    }
    json_data = json.dumps(data)
    return render(request, "iplapi/economy.html", context={"data":json_data})


def batting_avg(request):
    matches_data = queried_data.batting_average()
    data = {
        "matches_data":dict(matches_data),
        "title":"Top Batting Average for 2012",
        "text":"Batting Average",
        "bottom":"Batsman"
    }
    json_data = json.dumps(data)
    return render(request, "iplapi/batting_avg.html", context={"data":json_data})


