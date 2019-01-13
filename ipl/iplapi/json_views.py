from django.http import JsonResponse
import json
from .data import DataFromDb


data = DataFromDb()


# Create your views here.
def matches_per_season(request):
    context = data.matches_per_season()
    return JsonResponse(context)


def wins_per_season(request):
    context = data.wins_per_season()
    return JsonResponse(context)


def extra_runs(request):
    context = data.extra_runs()
    return JsonResponse(context)


def economy(request):
    context = data.economy()
    return JsonResponse(context)


def batting_avg(request):
    context = data.batting_average()
    return JsonResponse(context)