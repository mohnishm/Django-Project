from django.db.models import Count, Sum, F, ExpressionWrapper, DecimalField, FloatField
from django.shortcuts import render
from .models import Matches, Deliveries
from django.http import JsonResponse
import json
from collections import Counter


def Home(request):
    return render(request, "iplapi/home.html")


def matches_per_season(request):
    all_matches = Matches.objects.all()
    count = Counter([match.season for match in all_matches])
    context = {"matches_per_season": count}
    return JsonResponse(context)


def matches_per_season_charts(request):
    all_matches = Matches.objects.all()
    count = Counter([match.season for match in all_matches])
    context = {"matches_per_season": count}
    data = {
        "matches_data":dict(context),
        "title":"Matches Per Season",
        "text":"Number of Matches",
        "bottom":"Seasons"
    }
    json_data = json.dumps(data)
    return render(request, "iplapi/matches.html", context={"data":json_data})


def wins_per_season(request):
    winners_in_season =  Matches.objects.values('season', 'winner').annotate(Count("winner")).order_by("season")
    seasons = set(obj["season"] for obj in Matches.objects.values('season'))
    context = {season:[] for season in seasons}
    for data in winners_in_season:
        if data["season"] in context and data["winner"] != "":
            context[data["season"]].append({"team":data["winner"],"total_wins":data["winner__count"]})

    return JsonResponse(context)

def wins_per_season_charts(request):
    winners_in_season =  Matches.objects.values('season', 'winner').annotate(Count("winner")).order_by("season")
    seasons = set(obj["season"] for obj in Matches.objects.values('season'))
    context = {season:[] for season in seasons}
    for data in winners_in_season:
        if data["season"] in context and data["winner"] != "":
            context[data["season"]].append({"team":data["winner"],"total_wins":data["winner__count"]})
    data = {
        "matches_data":dict(context),
        "title":"Wins per team for every season ",
        "text":"Number of wins",
        "bottom":"Seasons"
    }
    json_data = json.dumps(data)
    return render(request, "iplapi/winsperseason.html", context={"data":json_data})


def extra_runs(request):
    extraruns_by_team = Matches.objects.filter(season=2016).annotate(bowling_team=F("deliveries__bowling_team")).values("bowling_team").annotate(extra_runs=Sum("deliveries__extra_runs"))
    context = {"extra_runs_2016":list(extraruns_by_team)}
    
    return JsonResponse(context)


def extra_runs_charts(request):
    extraruns_by_team = Matches.objects.filter(season=2016).annotate(bowling_team=F("deliveries__bowling_team")).values("bowling_team").annotate(extra_runs=Sum("deliveries__extra_runs"))
    context = {"extra_runs_2016":list(extraruns_by_team)}
    data = {
        "matches_data":dict(context),
        "title":"Extra runs conceded by each team in 2016",
        "text":"Extra runs",
        "bottom":"teams"
    }
    json_data = json.dumps(data)
    return render(request, "iplapi/extraruns.html", context={"data":json_data})


def economy(request):
    top_economical_bowler = Matches.objects.filter(season=2015).annotate(bowler=F("deliveries__bowler")).values("bowler").annotate(economy=ExpressionWrapper(Sum("deliveries__total_runs")/(Count("deliveries__ball")/6), output_field=DecimalField())).order_by("economy")[:5]
    top_economical_bowler = [{"bowler":query["bowler"], "economy":round(float(query["economy"]),2)} for query in top_economical_bowler]
    context = {"top_economical_bowler":list(top_economical_bowler)}
    
    return JsonResponse(context)


def economy_charts(request):
    top_economical_bowler = Matches.objects.filter(season=2015).annotate(bowler=F("deliveries__bowler")).values("bowler").annotate(economy=ExpressionWrapper(Sum("deliveries__total_runs")/(Count("deliveries__ball")/6), output_field=DecimalField())).order_by("economy")[:5]
    top_economical_bowler = [{"bowler":query["bowler"], "economy":round(float(query["economy"]),2)} for query in top_economical_bowler]
    context = {"top_economical_bowler":list(top_economical_bowler)}
    data = {
        "matches_data":dict(context),
        "title":"Top economical bowlers of 2015",
        "text":"Economy",
        "bottom":"Bowlers"
    }
    json_data = json.dumps(data)
    return render(request, "iplapi/economy.html", context={"data":json_data})


def batting_average(request):
    top_batsmen = Matches.objects.filter(season=2012).annotate(batsman=F("deliveries__batsman")).values("batsman").annotate(batsman_avg=ExpressionWrapper(Sum("deliveries__batsman_runs")/Count(F("deliveries__match_id"), distinct=True),output_field=FloatField())).order_by("-batsman_avg")[:5]
    top_average = [{"batsman": query["batsman"], "average": round(query["batsman_avg"], 2)} for query in top_batsmen]
    context = {"top_batting_average": top_average}

    return JsonResponse(context)


def batting_average_charts(request):
    top_batsmen = Matches.objects.filter(season=2012).annotate(batsman=F("deliveries__batsman")).values("batsman").annotate(batsman_avg=ExpressionWrapper(Sum("deliveries__batsman_runs")/Count(F("deliveries__match_id"), distinct=True),output_field=FloatField())).order_by("-batsman_avg")[:5]
    top_average = [{"batsman": query["batsman"], "average": round(query["batsman_avg"], 2)} for query in top_batsmen]
    context = {"top_batting_average": top_average}
    data = {
        "matches_data":dict(context),
        "title":"Top Batting Average for 2012",
        "text":"Batting Average",
        "bottom":"Batsman"
    }
    json_data = json.dumps(data)
    return render(request, "iplapi/batting_avg.html", context={"data":json_data})


