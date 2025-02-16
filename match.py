import random
from utils import calculate_home_advantage

def simulate_match(team1, team2, is_home_match=False):
    # Apply home advantage
    home_advantage_factor = calculate_home_advantage(is_home_match)

    # Calculate team strengths considering morale and home advantage
    team1_strength = team1.attack + team1.defense * team1.morale * home_advantage_factor
    team2_strength = team2.attack + team2.defense * team2.morale

    # Calculate probabilities of scoring
    total_strength = team1_strength + team2_strength
    team1_prob = team1_strength / total_strength
    team2_prob = team2_strength / total_strength

    # Simulate goals scored
    team1_goals = random.randint(0, int(team1_prob * 5))
    team2_goals = random.randint(0, int(team2_prob * 5))

    # Determine the result
    if team1_goals > team2_goals:
        result = 'win'
    elif team1_goals < team2_goals:
        result = 'loss'
    else:
        result = 'draw'

    return team1_goals, team2_goals, result
