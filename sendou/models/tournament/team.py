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
