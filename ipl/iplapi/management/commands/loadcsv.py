from django.core.management.base import BaseCommand, CommandError
from iplapi.models import Matches, Deliveries
from django.db import transaction
from django.db import connection

class Command(BaseCommand):
    help = 'Loads CSV file into MySQL'

    @transaction.atomic
    def handle(self, *args, **kwargs):

        curs = connection.cursor()
        
        res = curs.execute("LOAD DATA LOCAL INFILE '/home/mohnish/Projects/Python-Project-1/matches.csv' INTO TABLE matches FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES (ids, season, city, date, team1, team2, toss_winner, toss_decision, result, dl_applied, winner, win_by_runs, win_by_wickets, player_of_match, venue, umpire1, umpire2, umpire3);")
        
        result = curs.execute("LOAD DATA LOCAL INFILE '/home/mohnish/Projects/Python-Project-1/deliveries.csv' INTO TABLE deliveries FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES (match_id_id, inning, batting_team, bowling_team, over, ball, batsman, non_striker, bowler, is_super_over, wide_runs, bye_runs, legbye_runs, noball_runs, penalty_runs, batsman_runs, extra_runs, total_runs, player_dismissed, dismissal_kind, fielder);")
        
        if res:
            print (res)
        
        if result:
            print (result)