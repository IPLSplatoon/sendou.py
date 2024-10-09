"""
Standings  Model
"""
from typing import Optional


class StandingStats:
    """
    Stats for a Standing

    Attributes:
        set_wins (int): Set Wins
        set_losses (int): Set Loses
        map_wins (int): Map Wins
        map_losses (int): Map Loses
        points (int): Points
        wins_against_tied (int): Wins Against Tied
        buchholz_sets (Optional[int]): Buchholz Sets
        buchholz_maps (Optional[int]): Buchholz Maps
    """
    set_wins: int
    set_losses: int
    map_wins: int
    map_losses: int
    points: int
    wins_against_tied: int
    buchholz_sets: Optional[int]
    buchholz_maps: Optional[int]

    def __init__(self, set_wins: int, set_losses: int, map_wins: int, map_losses: int, points: int, wins_against_tied: int,
                 buchholz_sets: Optional[int] = None, buchholz_maps: Optional[int] = None):

        self.set_wins = set_wins
        self.set_losses = set_losses
        self.map_wins = map_wins
        self.map_losses = map_losses
        self.points = points
        self.wins_against_tied = wins_against_tied
        self.buchholz_maps = buchholz_maps
        self.buchholz_sets = buchholz_sets

    @classmethod
    def from_dict(cls, data: dict):
        """
        Returns a StandingStats object from a dictionary

        Args:
            data (dict): Dictionary

        Returns:
            StandingStats: StandingStats object
        """
        return cls(
            set_wins=data.get("setWins", 0),
            set_losses=data.get("setLosses", 0),
            map_wins=data.get("mapWins", 0),
            map_losses=data.get("mapLosses", 0),
            points=data.get("points", 0),
            wins_against_tied=data.get("winsAgainstTied", 0),
            buchholz_sets=data.get("buchholzSets", None),
            buchholz_maps=data.get("buchholzMaps", None)
        )


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
    stats: Optional[StandingStats]

    def __init__(self, data: dict):
        self.tournament_team_id = data.get("tournamentTeamId", 0)
        self.placement = data.get("placement", 0)
        if stats := data.get("stats", {}):
            self.stats = StandingStats.from_dict(stats)
        else:
            self.stats = None

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
