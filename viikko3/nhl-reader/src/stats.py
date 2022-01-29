class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players(nationality)

        players.sort(key=lambda x: x.total, reverse=True)

        return players