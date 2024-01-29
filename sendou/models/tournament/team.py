"""
Tournament Team
"""
from datetime import datetime
from typing import Optional, List

from ..stageMapList import StageWithMode


class TeamMember:
    user_id: int
    name: str
    discord_id: str
    avatar_url: Optional[str]
    captain: bool
    joined_at: datetime

    def __init__(self, data: dict):
        self.user_id = data.get("userId")
        self.name = data.get("name")
        self.discord_id = data.get("discordId")
        self.avatar_url = data.get("avatarUrl")
        self.captain = data.get("captain")
        self.joined_at = datetime.fromisoformat(data.get("joinedAt"))


class TournamentTeam:
    """
    GET /api/tournament/{tournamentId}/teams
    """
    id: int
    name: str
    registered_at: datetime
    checked_in: bool
    url: str
    seed: Optional[int]
    map_pool: Optional[List[StageWithMode]]
    members: List[TeamMember]

    def __init__(self, data: dict):
        self.id = data.get("id")
        self.name = data.get("name")
        self.registered_at = datetime.fromisoformat(data.get("registeredAt"))
        self.checked_in = data.get("checkedIn")
        self.url = data.get("url")
        self.seed = data.get("seed")
        map_pool = data.get("mapPool", [])
        if map_pool:
            self.map_pool = [StageWithMode(stage) for stage in map_pool]
        self.members = [TeamMember(member) for member in data.get("members")]
