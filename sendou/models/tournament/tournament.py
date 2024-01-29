"""
Tournament Info Model
"""
from datetime import datetime


class Team:
    registered_count: int
    checked_in_count: int


class Tournament:
    """
    GET /api/tournament/{tournamentId}
    """
    name: str
    url: str
    logo_url: str
    start_time: datetime
    teams: Team
