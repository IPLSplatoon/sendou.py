"""
Tournament Info Model
"""
from datetime import datetime
from typing import Any, Dict, List, Optional

from dateutil import parser

from sendou.models.baseModel import BaseModel
from sendou.requests import RequestsClient
from .bracket import Bracket, BracketType, BracketStanding
from .team import TournamentTeam
from sendou.models.organization import Organization


class TournamentTeamInfo:
    """
    Basic Info about the Tournament Teams Count & Checked In Count

    Attributes:
        registered_count (int): Registered Count
        checked_in_count (int): Checked In Count
    """
    registered_count: int
    checked_in_count: int

    def __init__(self, data: Dict[str, Any]):
        self.registered_count = data.get("registeredCount", 0)
        self.checked_in_count = data.get("checkedInCount", 0)


class TournamentBracket(BaseModel):
    """
    Sendou.ink Tournament Route Bracket Info

    Attributes:
        type (BracketType): Bracket Type
        name (str): Bracket Name
        _index (int): Bracket Index
        __tournament_id (int): Tournament ID
    """
    type: BracketType
    name: str
    _index: int
    __tournament_id: int

    def __init__(self, data: dict, index: int, tournament_id: int, request_client: RequestsClient):
        """
        Init
        :param data: Raw data from API
        :param index: Bracket Index from API
        :param tournament_id: Tournament ID bracket is associated with
        :param request_client: Request Client
        """
        super().__init__(data, request_client)
        self.type = BracketType(data.get("type", ""))
        self.name = data.get("name", "")
        self._index = index
        self.__tournament_id = tournament_id

    async def get_bracket_data(self) -> Optional[Bracket]:
        """
        Get the detailed bracket data, if bracket has details.

        *Here are cases where Brackets haven't been played so no data exists*

        Returns:
            (Optional[Bracket]): Bracket Data
        """
        path = Bracket.api_route(tournament_id=self.__tournament_id, bracket_index=self._index)
        data = await self._request_client.get_response(path)
        if not data.get("data", {}).get("match", []):
            return
        return Bracket(data, self._request_client)

    async def get_standings(self) -> List[BracketStanding]:
        """
        Get the bracket standings

        Returns:
            (List[BracketStanding]): List of Bracket Standings
        """
        path = BracketStanding.api_route(tournament_id=self.__tournament_id, bracket_index=self._index)
        data = await self._request_client.get_response(path)
        return [BracketStanding(standing) for standing in data["standings"]]


class Tournament(BaseModel):
    """
    Sendou.ink Tournament

    Attributes:
        id (str): Tournament ID
        name (str): Tournament Name
        url (str): Tournament URL
        logo_url (Optional[str]): Logo URL
        start_time (datetime): Start Time
        teams (TournamentTeamInfo): Tournament Team Info
        brackets (List[TournamentBracket]): Tournament Brackets
        organization_id (Optional[int]): Organization ID
    """
    id: int
    name: str
    url: str
    logo_url: Optional[str]
    start_time: datetime
    teams: TournamentTeamInfo
    brackets: List[TournamentBracket]
    organization_id: Optional[int]

    def __init__(self, id: int, data: dict, request_client: RequestsClient):
        """
        Init

        Args:
            id: Tournament ID
            data: Raw data from API
            request_client: Request Client
        """
        self.id = id
        super().__init__(data, request_client)
        self.name = data.get("name", "")
        self.url = data.get("url", "")
        self.logo_url = data.get("logoUrl", None)
        self.start_time = parser.isoparse(data.get("startTime", ""))
        self.teams = TournamentTeamInfo(data.get("teams", {}))
        self.brackets = [TournamentBracket(bracket, index, self.id, request_client) for index, bracket in
                         enumerate(data.get("brackets", []))]
        self.organization_id = data.get("organizationId", None)

    async def get_teams(self) -> List[TournamentTeam]:
        """
        Get the teams for the tournament

        Returns:
            (List[TournamentTeam]): List of Tournament Teams
        """
        path = TournamentTeam.api_route(tournament_id=self.id)
        data = await self._request_client.get_response(path)
        return [TournamentTeam(team, self._request_client) for team in data]

    async def get_organization(self) -> Optional[Organization]:
        """
        Get the organization for the tournament

        Returns:
            (Optional[Organization]): Organization (None if not found)
        """
        if self.organization_id is None:
            return None
        path = Organization.api_route(org_id=self.organization_id)
        data = await self._request_client.get_response(path=path)
        return Organization.from_dict(data, self._request_client)

    @staticmethod
    def api_route(**kwargs) -> str:
        """
        Returns API route for the model

        Args:
            tournament_id (str): Tournament ID

        Returns:
            str: API Route
        """
        return f"api/tournament/{kwargs.get('tournament_id')}"
