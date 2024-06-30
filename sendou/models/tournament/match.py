"""
Tournament Match Model
"""
from sendou.models.baseModel import BaseModel
from sendou.requests import RequestsClient

from typing import Optional, List, Union
from enum import Enum

from ..stageMapList import StageWithMode


class MapListSourceEnum(Enum):
    """
    Where Map was sourced from

    "DEFAULT" if it was a default map, something went wrong with the algorithm typically
    "TIEBREAKER" if it was a tiebreaker map (selected by the TO)
    "BOTH" both teams picked the map
    """
    DEFAULT = "DEFAULT"
    TIEBREAKER = "TIEBREAKER"
    BOTH = "BOTH"


class MapListMap:
    """
    Map in a Map List
    """
    map: StageWithMode
    # One of the following:
    # id of the team that picked the map
    # "DEFAULT" if it was a default map, something went wrong with the algorithm typically
    # "TIEBREAKER" if it was a tiebreaker map (selected by the TO)
    # "BOTH" both teams picked the map
    source: Union[int, MapListSourceEnum]
    winner_team_id: Optional[int]
    participated_user_ids: List[int]

    def __init__(self, data: dict):
        self.map = StageWithMode(data.get("map", {}))
        source = data.get("source")
        if isinstance(source, int):
            self.source = source
        else:
            self.source = MapListSourceEnum(source)
        self.winner_team_id = data.get("winnerTeamId", None)
        self.participated_user_ids = data.get("participatedUserIds", [])


class MatchTeam:
    """
    Team in a Match

    Attributes:
        id (int): Team ID
        score (int): Team Score
    """
    id: int
    score: int

    def __init__(self, data: dict):
        self.id = data.get("id", 0)
        self.score = data.get("score", 0)


class Match(BaseModel):
    """
    A Tournament Match

    Attributes:
        team_one (Optional[MatchTeam]): Team One
        team_two (Optional[MatchTeam]): Team Two
        map_list (List[MapListMap]): Map List
        url (str): Match URL
    """
    team_one: Optional[MatchTeam]
    team_two: Optional[MatchTeam]
    map_list: List[MapListMap]
    url: str

    def __init__(self, data: dict, request_client: RequestsClient):
        super().__init__(data, request_client)
        self.team_one = MatchTeam(data.get("teamOne", {}))
        self.team_two = MatchTeam(data.get("teamTwo", {}))
        self.map_list = [MapListMap(m) for m in data.get("mapList", [])]
        self.url = data.get("url", "")

    @staticmethod
    def api_route(**kwargs) -> str:
        """
        Get the API route

        Args:
            match_id (int): Match ID

        Returns:
            str: API Route
        """
        return f"api/tournament-match/{kwargs.get('match_id')}"
