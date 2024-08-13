"""
Standings  Model
"""
from typing import Optional


class StandingStats:
    """
    Stats for a Standing

    Attributes:
        set_wins (int): Set Wins
        set_loses (int): Set Loses
        map_wins (int): Map Wins
        map_loses (int): Map Loses
        points (int): Points
        wins_against_tied (int): Wins Against Tied
        buchholz_sets (Optional[int]): Buchholz Sets
        buchholz_maps (Optional[int]): Buchholz Maps
    """
    set_wins: int
    set_loses: int
    map_wins: int
    map_loses: int
    points: int
    wins_against_tied: int
    buchholz_sets: Optional[int]
    buchholz_maps: Optional[int]

    def __init__(self, data: dict):
        self.set_wins = data.get("setWins", 0)
        self.set_loses = data.get("setLoses", 0)
        self.map_wins = data.get("mapWins", 0)
        self.map_loses = data.get("mapLoses", 0)
        self.points = data.get("points", 0)
        self.wins_against_tied = data.get("winsAgainstTied", 0)
        self.buchholz_sets = data.get("buchholzSets", None)
        self.buchholz_maps = data.get("buchholzMaps", None)


class BracketStanding:
    """
    Represents a Team's standing in a bracket

    Attributes:
        tournament_team_id (int): Tournament Team ID
        placement (int): Placement
        stats (StandingStats): Standing Stats
    """
    tournament_team_id: int
    placement: int
    stats: StandingStats

    def __init__(self, data: dict):
        self.tournament_team_id = data.get("tournamentTeamId", 0)
        self.placement = data.get("placement", 0)
        self.stats = StandingStats(data.get("stats", {}))

    @staticmethod
    def api_route(**kwargs) -> str:
        """
        Returns API route for the model

        Args:
            tournament_id (str): Tournament ID
            bracket_index (int): Bracket Index

        Returns:
            str: API Route
        """
        return f"api/tournament/{kwargs.get('tournament_id')}/brackets/{kwargs.get('bracket_index')}/standings"
