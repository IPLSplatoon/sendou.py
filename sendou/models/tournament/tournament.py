"""
Tournament Info Model
"""
from datetime import datetime
from dateutil import parser


class Team:
    registered_count: int
    checked_in_count: int

    def __init__(self, data: dict):
        self.registered_count = data.get("registeredCount")
        self.checked_in_count = data.get("checkedInCount")


class Tournament:
    """
    GET /api/tournament/{tournamentId}
    """
    name: str
    url: str
    logo_url: str
    start_time: datetime
    teams: Team

    def __init__(self, data: dict):
        self.name = data.get("name")
        self.url = data.get("url")
        self.logo_url = data.get("logoUrl")
        self.start_time = parser.isoparse(data.get("startTime"))
        self.teams = Team(data.get("teams"))
