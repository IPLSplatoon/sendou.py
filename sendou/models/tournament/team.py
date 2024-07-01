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
    """
    Member of a Tournament Team

    Attributes:
        user_id (int): User ID
        name (str): Member's Name
        discord_id (str): Discord ID
        battlefy (Optional[str]): Battlefy ID
        avatar_url (Optional[str]): Avatar URL
        captain (bool): Is Captain
        joined_at (datetime): Joined At
    """
    user_id: int
    name: str
    discord_id: str
    battlefy: Optional[str]
    avatar_url: Optional[str]
    captain: bool
    joined_at: datetime

    def __init__(self, data: dict, request_client: RequestsClient):
        super().__init__(data, request_client)
        self.user_id = data.get("userId", 0)
        self.name = data.get("name", "")
        self.discord_id = data.get("discordId", "")
        self.battlefy = data.get("battlefy", None)
        self.avatar_url = data.get("avatarUrl", None)
        self.captain = data.get("captain", False)
        self.joined_at = parser.isoparse(data.get("joinedAt", ""))

    async def get_user(self) -> User:
        """
        Get the User object for the member

        Returns:
            (User): User Object
        """
        path = User.api_route(user_id=self.user_id)
        data = await self._request_client.get_response(path)
        return User(data, self._request_client)


class TournamentTeam(BaseModel):
    """
    A Tournament Team

    Attributes:
        id (int): Team ID
        name (str): Team Name
        registered_at (datetime): Registered At
        checked_in (bool): Checked In
        url (str): Team URL
        team_page_url (Optional[str]): Team Page URL
        logo_url (Optional[str]): Logo URL
        seed (Optional[int]): Seed
        map_pool (Optional[List[StageWithMode]]): Map Pool
        members (List[TeamMember]): Team Members
    """
    id: int
    name: str
    registered_at: datetime
    checked_in: bool
    url: str
    team_page_url: Optional[str]
    logo_url: Optional[str]
    seed: Optional[int]
    map_pool: Optional[List[StageWithMode]]
    members: List[TeamMember]

    def __init__(self, data: dict, request_client: RequestsClient):
        """
        Init
        :param data: Raw data from API
        :param request_client: Request Client
        """
        super().__init__(data, request_client)
        self.id = data.get("id", 0)
        self.name = data.get("name", "")
        self.registered_at = parser.isoparse(data.get("registeredAt", ""))
        self.checked_in = data.get("checkedIn", False)
        self.url = data.get("url", "")
        self.team_page_url = data.get("teamPageUrl", None)
        self.logo_url = data.get("logoUrl", None)
        self.seed = data.get("seed")
        map_pool = data.get("mapPool", [])
        if map_pool:
            self.map_pool = [StageWithMode(stage) for stage in map_pool]
        self.members = [TeamMember(member, request_client) for member in data.get("members", [])]

    @staticmethod
    def api_route(**kwargs) -> str:
        """
        Get the API route

        Args:
            tournament_id (int): Tournament ID

        Returns:
        """
        return f"api/tournament/{kwargs.get('tournament_id')}/teams"
