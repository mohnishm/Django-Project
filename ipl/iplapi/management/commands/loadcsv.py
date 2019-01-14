from django.core.management.base import BaseCommand, CommandError
from iplapi.models import Matches, Deliveries
from django.db import transaction
from django.db import connection
import csv
from iplapi.models import Matches, Deliveries

class Command(BaseCommand):
    help = 'Loads CSV file into MySQL'

    def handle(self, *args, **kwargs):

        match_reader = csv.DictReader(open("/home/mohnish/Projects/Python-Project-1/matches.csv"))
        delivery_reader = csv.DictReader(open("/home/mohnish/Projects/Python-Project-1/deliveries.csv"))
        
        with transaction.atomic():
            for row in match_reader:
                match = Matches(ids=row["id"], season=row["season"], city=row["city"], date=row["date"], team1=row["team1"], team2=row["team2"], toss_winner=row["toss_winner"], toss_decision=row["toss_decision"], result=row["result"], dl_applied=row["dl_applied"], winner=row["winner"], win_by_runs=row["win_by_runs"], win_by_wickets=row["win_by_wickets"], player_of_match=row["player_of_match"], venue=row["venue"], umpire1=row["umpire1"], umpire2=row["umpire2"], umpire3=row["umpire3"])

                match.save()

        
        with transaction.atomic():
            for row in delivery_reader:
                deliv = Deliveries(match_id_id=row["match_id"], inning=row["inning"], batting_team=row["batting_team"], bowling_team=row["bowling_team"], over=row["over"], ball=row["ball"], batsman=row["batsman"], non_striker=row["non_striker"], bowler=row["bowler"], is_super_over=row["is_super_over"], wide_runs=row["wide_runs"], bye_runs=row["bye_runs"], legbye_runs=row["legbye_runs"], noball_runs=row["noball_runs"], penalty_runs=row["penalty_runs"], batsman_runs=row["batsman_runs"], extra_runs=row["extra_runs"], total_runs=row["total_runs"], player_dismissed=row["player_dismissed"], dismissal_kind=row["dismissal_kind"], fielder=row["fielder"])

                deliv.save()