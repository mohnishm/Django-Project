from django.db.models import Count, Sum, F, ExpressionWrapper, DecimalField, FloatField
from django.shortcuts import render
from .models import Matches, Deliveries
from django.http import JsonResponse
import json
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def Home(request):
    return render(request, "iplapi/home.html")


@cache_page(CACHE_TTL)
def matches_per_season(request):
    count = Matches.objects.values('season').annotate(matches=Count("season")).order_by("season")
    context = {"matches_per_season": list(count)}
    return JsonResponse(context)


@cache_page(CACHE_TTL)
def matches_per_season_charts(request):
    count = Matches.objects.values('season').annotate(matches=Count("season")).order_by("season")
    context = {"matches_per_season": list(count)}
    data = (context)
    json_data = json.dumps(data)
    return render(request, "iplapi/matches.html", context={"data":json_data})


@cache_page(CACHE_TTL)
def wins_per_season(request):
    winners_in_season =  Matches.objects.values('season', 'winner').annotate(Count("winner")).order_by("season")
    seasons = set(obj["season"] for obj in Matches.objects.values('season'))
    context = {season:[] for season in seasons}
    for data in winners_in_season:
        if data["season"] in context and data["winner"] != "":
            context[data["season"]].append({"team":data["winner"],"total_wins":data["winner__count"]})

    return JsonResponse(context)


@cache_page(CACHE_TTL)
def wins_per_season_charts(request):
    winners_in_season =  Matches.objects.values('season', 'winner').annotate(Count("winner")).order_by("season")
    seasons = set(obj["season"] for obj in Matches.objects.values('season'))
    context = {season:[] for season in seasons}
    for data in winners_in_season:
        if data["season"] in context and data["winner"] != "":
            context[data["season"]].append({"team":data["winner"],"total_wins":data["winner__count"]})
    data = dict(context)
    json_data = json.dumps(data)
    return render(request, "iplapi/winsperseason.html", context={"data":json_data})


@cache_page(CACHE_TTL)
def extra_runs(request):
    extraruns_by_team = Matches.objects.filter(season=2016).annotate(bowling_team=F("deliveries__bowling_team")).values("bowling_team").annotate(extra_runs=Sum("deliveries__extra_runs"))
    context = {"extra_runs_2016":list(extraruns_by_team)}
    
    return JsonResponse(context)


@cache_page(CACHE_TTL)
def extra_runs_charts(request):
    extraruns_by_team = Matches.objects.filter(season=2016).annotate(bowling_team=F("deliveries__bowling_team")).values("bowling_team").annotate(extra_runs=Sum("deliveries__extra_runs"))
    context = {"extra_runs_2016":list(extraruns_by_team)}
    data = dict(context)
    json_data = json.dumps(data)
    return render(request, "iplapi/extraruns.html", context={"data":json_data})


@cache_page(CACHE_TTL)
def economy(request):
    top_economical_bowler = Matches.objects.filter(season=2015).annotate(bowler=F("deliveries__bowler")).values("bowler").annotate(economy=ExpressionWrapper(Sum("deliveries__total_runs")/(Count("deliveries__ball")/6), output_field=DecimalField())).order_by("economy")[:5]
    top_economical_bowler = [{"bowler":query["bowler"], "economy":round(float(query["economy"]),2)} for query in top_economical_bowler]
    context = {"top_economical_bowler":list(top_economical_bowler)}
    
    return JsonResponse(context)


@cache_page(CACHE_TTL)
def economy_charts(request):
    top_economical_bowler = Matches.objects.filter(season=2015).annotate(bowler=F("deliveries__bowler")).values("bowler").annotate(economy=ExpressionWrapper(Sum("deliveries__total_runs")/(Count("deliveries__ball")/6), output_field=DecimalField())).order_by("economy")[:5]
    top_economical_bowler = [{"bowler":query["bowler"], "economy":round(float(query["economy"]),2)} for query in top_economical_bowler]
    context = {"top_economical_bowler":list(top_economical_bowler)}
    data = dict(context)
    json_data = json.dumps(data)
    return render(request, "iplapi/economy.html", context={"data":json_data})


@cache_page(CACHE_TTL)
def batting_average(request):
    top_batsmen = Matches.objects.filter(season=2012).annotate(batsman=F("deliveries__batsman")).values("batsman").annotate(batsman_avg=ExpressionWrapper(Sum("deliveries__batsman_runs")/Count(F("deliveries__match_id"), distinct=True),output_field=FloatField())).order_by("-batsman_avg")[:5]
    top_average = [{"batsman": query["batsman"], "average": round(query["batsman_avg"], 2)} for query in top_batsmen]
    context = {"top_batting_average": top_average}

    return JsonResponse(context)


@cache_page(CACHE_TTL)
def batting_average_charts(request):
    top_batsmen = Matches.objects.filter(season=2012).annotate(batsman=F("deliveries__batsman")).values("batsman").annotate(batsman_avg=ExpressionWrapper(Sum("deliveries__batsman_runs")/Count(F("deliveries__match_id"), distinct=True),output_field=FloatField())).order_by("-batsman_avg")[:5]
    top_average = [{"batsman": query["batsman"], "average": round(query["batsman_avg"], 2)} for query in top_batsmen]
    context = {"top_batting_average": top_average}
    data = dict(context)
    json_data = json.dumps(data)
    return render(request, "iplapi/batting_avg.html", context={"data":json_data})
