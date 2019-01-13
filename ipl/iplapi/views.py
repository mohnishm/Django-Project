from django.db.models import Count, Sum, F, ExpressionWrapper, DecimalField, FloatField
from django.shortcuts import render
from .models import Matches, Deliveries
from django.http import HttpResponse
import json
from collections import Counter


# Create your views here.
def matches_per_season(request):
    all_matches = Matches.objects.all()
    count = Counter([match.season for match in all_matches])
    context = {"matches_per_season": count}
    return HttpResponse(json.dumps(context), content_type="application/json")


def wins_per_season(request):
    winners_in_season =  Matches.objects.values('season', 'winner').annotate(Count("winner")).order_by("season")
    seasons = set(obj["season"] for obj in Matches.objects.values('season'))
    context = {season:[] for season in seasons}
    for data in winners_in_season:
        if data["season"] in context and data["winner"] != "":
           context[data["season"]].append({"team":data["winner"],"total_wins":data["winner__count"]})

    return HttpResponse(json.dumps(context), content_type="application/json")


def extra_runs(request):
    extraruns_by_team = Matches.objects.filter(season=2016).annotate(bowling_team=F("deliveries__bowling_team")).values("bowling_team").annotate(extra_runs=Sum("deliveries__extra_runs"))
    context = {"2016_extra_runs":list(extraruns_by_team)}
    return HttpResponse(json.dumps(context), content_type="application/json")

def economy(request):
    top_economical_bowler = Matches.objects.filter(season=2015).annotate(bowler=F("deliveries__bowler")).values("bowler").annotate(economy=ExpressionWrapper(Sum("deliveries__total_runs")/(Count("deliveries__ball")/6), output_field=DecimalField())).order_by("economy")[:5]
    top_economical_bowler = [{"bowler":query["bowler"], "economy":round(float(query["economy"]),2)} for query in top_economical_bowler]

    context = {"top_economical_bowler":list(top_economical_bowler)}
    return HttpResponse(json.dumps(context), content_type="application/json")


def batting_average(request):
    top_batsmen = Matches.objects.filter(season=2012).annotate(batsman=F("deliveries__batsman")).values("batsman").annotate(batsman_avg=ExpressionWrapper(Sum("deliveries__batsman_runs")/Count(F("deliveries__match_id"), distinct=True),output_field=FloatField())).order_by("-batsman_avg")[:5]
        
    top_average = [{"batsman": query["batsman"], "average": round(query["batsman_avg"], 2)} for query in top_batsmen]

    return HttpResponse(json.dumps(top_average), content_type="application/json")