class Team:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.morale = 1.0  # Initial morale
        self.played = 0 # Number of matches played
        self.points = 0
        self.goals_for = 0
        self.goals_against = 0

    def update_morale(self, result): # result can be 'win', 'loss', or 'draw'
        if result == 'win':
            self.morale += 0.1
        elif result == 'loss':
            self.morale -= 0.1
        else:
            self.morale += 0.05
        
        self.morale = max(0.5, min(1.5, self.morale)) # Keep morale within reasonable bounds
