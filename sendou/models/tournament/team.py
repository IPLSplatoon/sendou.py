"""
Tournament Team
"""
from sendou.models.baseModel import BaseModel
from sendou.requests import RequestsClient

from datetime import datetime
from dateutil import parser
from typing import Optional, List

from ..stageMapList import StageWithMode
from ..user import User


class TeamMember(BaseModel):
    user_id: int
    name: str
    discord_id: str
    avatar_url: Optional[str]
    captain: bool
    joined_at: datetime

    def __init__(self, data: dict, request_client: RequestsClient):
        super().__init__(data, request_client)
        self.user_id = data.get("userId", 0)
        self.name = data.get("name", "")
        self.discord_id = data.get("discordId", "")
        self.avatar_url = data.get("avatarUrl", "")
        self.captain = data.get("captain", False)
        self.joined_at = parser.isoparse(data.get("joinedAt", ""))

    async def get_user(self) -> User:
        path = User.api_route(user_id=self.user_id)
        data = await self._request_client.get_response(path)
        return User(data, self._request_client)


class TournamentTeam(BaseModel):
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

    def __init__(self, data: dict, request_client: RequestsClient):
        super().__init__(data, request_client)
        self.id = data.get("id", 0)
        self.name = data.get("name", "")
        self.registered_at = parser.isoparse(data.get("registeredAt", ""))
        self.checked_in = data.get("checkedIn", False)
        self.url = data.get("url", "")
        self.seed = data.get("seed")
        map_pool = data.get("mapPool", [])
        if map_pool:
            self.map_pool = [StageWithMode(stage) for stage in map_pool]
        self.members = [TeamMember(member, request_client) for member in data.get("members", [])]

    @staticmethod
    def api_route(**kwargs) -> str:
        """
        :param kwargs:
        :Keyword Arguments:
            tournament_id: str
        :return:
        """
        return f"api/tournament/{kwargs.get('tournament_id')}/teams"
