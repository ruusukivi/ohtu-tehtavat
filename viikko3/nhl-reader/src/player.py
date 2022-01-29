class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.total = goals+assists
    
    def __str__(self):
        player = f"{self.name:20} {self.team} {str(self.goals):2} + {str(self.assists):2} = {self.total}"
        return player
