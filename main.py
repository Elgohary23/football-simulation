import itertools
import random
from team import Team  # Import the Team class
from match import simulate_match  # Import the simulate_match function

teams = [
    Team("Arsenal", 14, 12),
    Team("Aston Villa", 12, 10),
    Team("Brentford", 11, 11),
    Team("Brighton & Hove Albion", 10, 12),
    Team("Burnley", 9, 13),
    Team("Chelsea", 15, 11),
    Team("Crystal Palace", 10, 13),
    Team("Everton", 12, 12),
    Team("Leeds United", 13, 13),
    Team("Leicester City", 14, 12),
    Team("Liverpool", 16, 10),
    Team("Manchester City", 17, 9),
    Team("Manchester United", 15, 11),
    Team("Newcastle United", 10, 14),
    Team("Norwich City", 8, 15),
    Team("Southampton", 11, 13),
    Team("Tottenham Hotspur", 13, 11),
    Team("Watford", 9, 14),
    Team("West Ham United", 14, 12),
    Team("Wolverhampton Wanderers", 11, 11),
]

def round_robin(teams):
    """Generates a round-robin tournament schedule."""
    fixtures = []
    n = len(teams)
    for i in range(n):
        for j in range(n):
            if i != j:
                fixtures.append((teams[i], teams[j]))
    return fixtures

fixtures = round_robin(teams)

# Simulate the matches and update the league table
for team in teams:
    team.points = 0
    team.goals_for = 0
    team.goals_against = 0
    team.played = 0

for fixture in fixtures:
    team1, team2 = fixture
    is_home_match = True # team1 is always home team in this version
    team1_goals, team2_goals, result = simulate_match(team1, team2, is_home_match)
    print(f"{team1.name} vs {team2.name}: {team1_goals} - {team2_goals}")

    team1.goals_for += team1_goals
    team1.goals_against += team2_goals
    team2.goals_for += team2_goals
    team2.goals_against += team1_goals
    team1.played += 1
    team2.played += 1

    if result == "win":
        team1.points += 3
        team1.update_morale("win")
        team2.update_morale("loss")
    elif result == "loss":
        team2.points += 3
        team1.update_morale("loss")
        team2.update_morale("win")
    else:
        team1.points += 1
        team2.points += 1
        team1.update_morale("draw")
        team2.update_morale("draw")


# Print the league table
print("\nLeague Table:\n")

sorted_league_table = sorted(teams, key=lambda team: team.points, reverse=True)

for team in sorted_league_table:
    print(f"{team.name}: Points: {team.points}, Played: {team.played}, Goals For: {team.goals_for}, Goals Against: {team.goals_against}")
