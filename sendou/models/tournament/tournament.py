"""
Tournament Info Model
"""
from sendou.models.baseModel import BaseModel
from sendou.requests import RequestsClient
from .team import TournamentTeam
from .bracket import Bracket

from datetime import datetime
from dateutil import parser
from typing import Any, Dict, List, Optional
from enum import Enum


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


class BracketType(Enum):
    """
    Bracket Types

    Values:
        SINGLE_ELIMINATION: Single Elimination Bracket
        DOUBLE_ELIMINATION: Double Elimination Bracket
        ROUND_ROBIN: Round Robin Bracket
        SWISS: Swiss Bracket
    """
    SINGLE_ELIMINATION = "single_elimination"
    DOUBLE_ELIMINATION = "double_elimination"
    ROUND_ROBIN = "round_robin"
    SWISS = "swiss"


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

    async def get_bracket_data(self) -> Bracket:
        """
        Get the detailed bracket data

        Returns:
            (Bracket): Bracket Data
        """
        path = Bracket.api_route(tournament_id=self.__tournament_id, bracket_index=self._index)
        data = await self._request_client.get_response(path)
        return Bracket(data, self._request_client)


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
    """
    id: int
    name: str
    url: str
    logo_url: Optional[str]
    start_time: datetime
    teams: TournamentTeamInfo
    brackets: List[TournamentBracket]

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

    async def get_teams(self) -> List[TournamentTeam]:
        """
        Get the teams for the tournament

        Returns:
            (List[TournamentTeam]): List of Tournament Teams
        """
        path = TournamentTeam.api_route(tournament_id=self.id)
        data = await self._request_client.get_response(path)
        return [TournamentTeam(team, self._request_client) for team in data]

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
