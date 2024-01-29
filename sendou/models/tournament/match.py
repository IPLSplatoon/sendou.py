"""
Tournament Match Model
"""
from typing import Optional, List, Union
from enum import Enum

from ..stageMapList import StageWithMode


class MapListSourceEnum(Enum):
    DEFAULT = "DEFAULT"
    TIEBREAKER = "TIEBREAKER"
    BOTH = "BOTH"


class MapListMap:
    map: StageWithMode
    # One of the following:
    # id of the team that picked the map
    # "DEFAULT" if it was a default map, something went wrong with the algorithm typically
    # "TIEBREAKER" if it was a tiebreaker map (selected by the TO)
    # "BOTH" both teams picked the map
    source: Union[int, MapListSourceEnum]
    winner_team_id: Optional[int]
    participated_user_ids: List[int]


class TournamentMatchTeam:
    id: int
    score: int


class TournamentMatch:
    """
    GET /api/tournament/{tournamentId}
    """
    team_one: Optional[TournamentMatchTeam]
    team_two: Optional[TournamentMatchTeam]
    map_list: List[MapListMap]
    url: str
