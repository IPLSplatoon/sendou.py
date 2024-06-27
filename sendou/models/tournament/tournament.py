"""
Tournament Info Model
"""
from sendou.models.baseModel import BaseModel
from sendou.requests import RequestsClient
from .team import TournamentTeam
from .bracket import Bracket

from datetime import datetime
from dateutil import parser
from typing import Any, Dict, List
from enum import Enum


class TournamentTeamInfo:
    registered_count: int
    checked_in_count: int

    def __init__(self, data: Dict[str, Any]):
        self.registered_count = data.get("registeredCount", 0)
        self.checked_in_count = data.get("checkedInCount", 0)


class BracketType(Enum):
    SINGLE_ELIMINATION = "single_elimination"
    DOUBLE_ELIMINATION = "double_elimination"
    ROUND_ROBIN = "round_robin"
    SWISS = "swiss"


class TournamentBracket(BaseModel):
    type: BracketType
    name: str
    _index: int
    __tournament_id: str

    def __init__(self, data: dict, index: int, tournament_id: str, request_client: RequestsClient):
        super().__init__(data, request_client)
        self.type = BracketType(data.get("type", ""))
        self.name = data.get("name", "")
        self._index = index
        self.__tournament_id = tournament_id

    async def get_bracket_data(self) -> Bracket:
        """
        Get the bracket data
        :return:
        """
        path = Bracket.api_route(tournament_id=self.__tournament_id, bracket_index=self._index)
        data = await self._request_client.get_response(path)
        return Bracket(data, self._request_client)


class Tournament(BaseModel):
    """
    GET /api/tournament/{tournamentId}
    """
    id: str
    name: str
    url: str
    logo_url: str
    start_time: datetime
    teams: TournamentTeamInfo
    brackets: List[TournamentBracket]

    def __init__(self, id: str, data: dict, request_client: RequestsClient):
        self.id = id
        super().__init__(data, request_client)
        self.name = data.get("name", "")
        self.url = data.get("url", "")
        self.logo_url = data.get("logoUrl", "")
        self.start_time = parser.isoparse(data.get("startTime", ""))
        self.teams = TournamentTeamInfo(data.get("teams", {}))
        self.brackets = [TournamentBracket(bracket, index, self.id, request_client) for index, bracket in
                         enumerate(data.get("brackets", []))]

    async def get_teams(self) -> List[TournamentTeam]:
        """
        Get the teams for the tournament
        :return:
        """
        path = TournamentTeam.api_route(tournament_id=self.id)
        data = await self._request_client.get_response(path)
        return [TournamentTeam(team, self._request_client) for team in data]

    @staticmethod
    def api_route(**kwargs) -> str:
        """
        :param kwargs:
        :Keyword Arguments:
            tournament_id: str
        :return:
        """
        return f"api/tournament/{kwargs.get('tournament_id')}"
