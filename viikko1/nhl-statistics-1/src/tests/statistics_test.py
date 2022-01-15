import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_search_by_name(self):
        name = "Kurri"
        self.assertEqual(str(self.statistics.search(name)), "Kurri EDM 37 + 53 = 90")

    def test_search_by_name_not_found(self):
        name = "Kuri"
        self.assertEqual(str(self.statistics.search(name)), "None")

    def test_search_by_team(self):
        team = "DET"
        self.assertEqual(str(self.statistics.team(team)[0]), "Yzerman DET 42 + 56 = 98" )

    def test_top_player_is_Gretzky(self):
        self.assertEqual(str(self.statistics.top_scorers(1)[0]), "Gretzky EDM 35 + 89 = 124")