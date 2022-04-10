class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0
        self.score = ""

    def add_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points = self.player1_points + 1
        if player_name == self.player2_name:
            self.player2_points = self.player2_points + 1

    def get_player_score(self, points):
        if points == 0:
            return "Love"
        if points == 1:
            return "Fifteen"
        if points == 2:
            return "Thirty"
        return "Forty"

    def get_set_score(self):
        score_for_player1 = self.get_player_score(self.player1_points)
        score_for_player2 = self.get_player_score(self.player2_points)
        return score_for_player1 + "-" + score_for_player2

    def get_tied_set_score(self):
        if self.player1_points == 0:
            return "Love-All"
        if self.player1_points == 1:
            return "Fifteen-All"
        if self.player1_points == 2:
            return "Thirty-All"
        if self.player1_points == 3:
            return "Forty-All"
        return "Deuce"

    def get_last_set_score(self):
        point_difference = self.player1_points - self.player2_points
        if point_difference == 1:
            return"Advantage player1"
        if point_difference == -1:
            return "Advantage player2"
        if point_difference >= 2:
            return "Win for player1"
        return "Win for player2"

    def get_score(self):
        score = ""

        if self.player1_points == self.player2_points:
            score = self.get_tied_set_score()

        elif self.player1_points >= 4 or self.player2_points >= 4:
            score = self.get_last_set_score()

        else:
            score = self.get_set_score()

        return score
