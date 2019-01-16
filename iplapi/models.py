from django.db import models
import datetime

# Create your models here.
class Matches(models.Model):
    ids = models.IntegerField(primary_key=True)
    season = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    team1 = models.CharField(max_length=100, blank=True, null=True)
    team2 = models.CharField(max_length=100, blank=True, null=True)
    toss_winner = models.CharField(max_length=100, blank=True, null=True)
    toss_decision = models.CharField(max_length=100, blank=True, null=True)
    result = models.CharField(max_length=50, blank=True, null=True)
    dl_applied = models.IntegerField(blank=True, null=True)
    winner = models.CharField(max_length=100, blank=True, null=True)
    win_by_runs = models.IntegerField(blank=True, null=True)
    win_by_wickets = models.IntegerField(blank=True, null=True)
    player_of_match = models.CharField(max_length=100, blank=True, null=True)
    venue = models.CharField(max_length=200, blank=True, null=True)
    umpire1 = models.CharField(max_length=200, blank=True, null=True)
    umpire2 = models.CharField(max_length=200, blank=True, null=True)
    umpire3 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = "matches"
    
    def __str__(self):
        return self.ids


class Deliveries(models.Model):
    match_id = models.ForeignKey('Matches', on_delete=models.CASCADE, blank=True)
    inning = models.IntegerField(blank=True, null=True)
    batting_team = models.CharField(max_length=100, blank=True, null=True)
    bowling_team = models.CharField(max_length=100, blank=True, null=True)
    over = models.IntegerField(blank=True, null=True)
    ball = models.IntegerField(blank=True, null=True)
    batsman = models.CharField(max_length=100, blank=True, null=True)
    non_striker = models.CharField(max_length=100, blank=True, null=True)
    bowler = models.CharField(max_length=100, blank=True, null=True)
    is_super_over = models.IntegerField(blank=True, null=True)
    wide_runs = models.IntegerField(blank=True, null=True)
    bye_runs = models.IntegerField(blank=True, null=True)
    legbye_runs = models.IntegerField(blank=True, null=True)
    noball_runs = models.IntegerField(blank=True, null=True)
    penalty_runs = models.IntegerField(blank=True, null=True)
    batsman_runs = models.IntegerField(blank=True, null=True)
    extra_runs = models.IntegerField(blank=True, null=True)
    total_runs = models.IntegerField(blank=True, null=True)
    player_dismissed = models.CharField(max_length=100, blank=True, null=True)
    dismissal_kind = models.CharField(max_length=50, blank=True, null=True)
    fielder = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "deliveries"
    
    def __str__(self):
        return self.match_id