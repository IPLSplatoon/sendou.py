"""
Tournament Bracket Model
"""
from sendou.models.baseModel import BaseModel
from sendou.requests import RequestsClient

from typing import Any, Optional, List
from datetime import datetime, timezone

from .type import BracketType, RoundType, MatchResult
from sendou.models.tournament.match import Match


class BracketMeta:
    """
    Bracket Metadata

    Attributes:
        teams_per_group (Optional[int]): Teams per Group
        group_count (Optional[int]): Group Count
        round_count (Optional[int]): Round Count
    """
    teams_per_group: Optional[int]
    group_count: Optional[int]
    round_count: Optional[int]

    def __init__(self, data: dict):
        self.teams_per_group = data.get("teamsPerGroup", None)
        self.group_count = data.get("groupCount", None)
        self.round_count = data.get("roundCount", None)


class BracketSettings:
    """
    Bracket Settings

    Attributes:
        size (int): Bracket Size
        seed_ordering (List[str]): Seed Ordering
        consolation_final (Optional[bool]): Consolation Final
        round_robin_mode (Optional[str]): Round Robin Mode
        group_count (Optional[int]): Group Count
        grand_final (Optional[str]): Grand Final
    """
    _raw: dict
    size: int  # Size of bracket?
    seed_ordering: List[str]
    consolation_final: Optional[bool]
    round_robin_mode: Optional[str]
    group_count: Optional[int]
    grand_final: Optional[str]

    def __init__(self, data: dict):
        self._raw = data
        self.size = data.get("size", 0)
        self.seed_ordering = data.get("seedOrdering", [])
        self.consolation_final = data.get("consolationFinal", None)
        self.round_robin_mode = data.get("roundRobinMode", None)
        self.group_count = data.get("groupCount", None)
        self.grand_final = data.get("grandFinal", None)


class BracketStage:
    """
    Bracket Stage

    Attributes:
        id (int): Bracket Stage ID
        name (str): Bracket Stage Name
        number (int): Bracket Stage Number
        settings (Any): Bracket Stage Settings
        tournament_id (int): Tournament ID
        type (BracketType): Bracket Type
        created_at (Optional[datetime]): Created At
    """
    id: int
    name: str
    number: int
    settings: BracketSettings
    tournament_id: int
    type: BracketType
    created_at: Optional[datetime]  # Provided as unix timestamp

    def __init__(self, data: dict):
        self.id = data.get("id", 0)
        self.name = data.get("name", "")
        self.number = data.get("number", 0)
        self.settings = BracketSettings(data.get("settings", {}))
        self.tournament_id = data.get("tournament_id", 0)
        self.type = BracketType(data.get("type", ""))
        if created_at := data.get("createdAt", 0):
            self.created_at = datetime.fromtimestamp(created_at, tz=timezone.utc)


class BracketGroup:
    """
    Bracket Group

    Attributes:
        id (int): Bracket Group ID
        number (int): Bracket Group Number
        stage_id (int): Bracket Stage ID
    """
    id: int
    number: int
    stage_id: int

    def __init__(self, data: dict):
        self.id = data.get("id", 0)
        self.numbers = data.get("number", 0)
        self.stage_id = data.get("stage_id", 0)


class BracketRoundMap:
    """
    Bracket Round Map

    Attributes:
        count (int): Round Count
        type (RoundType): Round Type
    """
    count: int
    type: RoundType

    def __init__(self, data: dict):
        self.count = data.get("count", 0)
        self.type = RoundType(data.get("type", ""))


class BracketRound:
    """
    Bracket Round

    Attributes:
        id (int): Bracket Round ID
        group_id (int): Bracket Group ID
        number (int): Bracket Round Number
        stage_id (int): Bracket Stage ID
        maps (BracketRoundMap): Bracket Round Map Metadata
    """
    id: int
    group_id: int
    number: int
    stage_id: int
    maps: BracketRoundMap

    def __init__(self, data: dict):
        self.id = data.get("id", 0)
        self.group_id = data.get("group_id", 0)
        self.number = data.get("number", 0)
        self.stage_id = data.get("stage_id", 0)
        self.maps = BracketRoundMap(data.get("maps", {}))


class BracketMatchOpponent:
    """
    Bracket Match Opponent

    Attributes:
        id (int): Opponent ID
        position (int): Opponent Seed?
        score (int): Opponent Score
        result (MatchResult): Opponent Result
        totalPoints (int): Total Points (Swiss/RR)
    """
    id: int
    position: Optional[int]
    score: Optional[int]
    result: Optional[MatchResult]
    totalPoints: Optional[int]

    def __init__(self, data: dict):
        self.id = data.get("id", 0)
        if "position" in data:
            self.position = data.get("position", 0)
        if "score" in data:
            self.score = data.get("score", 0)
        if "result" in data:
            self.result = MatchResult(data.get("result", ""))
        if "totalPoints" in data:
            self.totalPoints = data.get("totalPoints", 0)


class BracketMatch(BaseModel):
    """
    Bracket Match

    Attributes:
        id (int): Bracket Match ID
        group_id (int): Bracket Group ID
        number (int): Bracket Match Number
        opponent1 (BracketMatchOpponent): Opponent 1
        opponent2 (Optional[BracketMatchOpponent]): Opponent 2
        round_id (int): Bracket Round ID
        stage_id (int): Bracket Stage ID
        status (int): Bracket Match Status
        lastGameFinishedAt (datetime): Last Game Finished At
        createdAt (datetime): Created At
    """
    id: int
    group_id: int
    number: int
    opponent1: Optional[BracketMatchOpponent]
    opponent2: Optional[BracketMatchOpponent]
    round_id: int
    stage_id: int
    status: int
    lastGameFinishedAt: Optional[datetime]  # Unix timestamp
    createdAt: Optional[datetime]  # Unix timestamp

    def __init__(self, data: dict, request_client: RequestsClient):
        super().__init__(data, request_client)
        self.id = data.get("id", 0)
        self.group_id = data.get("group_id", 0)
        self.number = data.get("number", 0)
        if data.get("opponent1", {}):
            self.opponent1 = BracketMatchOpponent(data.get("opponent1", {}))
        else:
            self.opponent1 = None
        if data.get("opponent2", {}):
            self.opponent2 = BracketMatchOpponent(data.get("opponent2", {}))
        else:
            self.opponent2 = None
        self.round_id = data.get("round_id", 0)
        self.stage_id = data.get("stage_id", 0)
        self.status = data.get("status", 0)
        if data.get("lastGameFinishedAt", None):
            self.lastGameFinishedAt = datetime.fromtimestamp(data.get("lastGameFinishedAt", 0), tz=timezone.utc)
        else:
            self.lastGameFinishedAt = None
        if data.get("createdAt", None):
            self.createdAt = datetime.fromtimestamp(data.get("createdAt", 0), tz=timezone.utc)
        else:
            self.createdAt = None

    async def get_match(self) -> Optional[Match]:
        """
        Get the match data

        Returns:
            (Match): Match Data
        """
        path = Match.api_route(match_id=self.id)
        data = await self._request_client.get_response(path)
        if data:
            return Match(data, self._request_client)


class BracketData(BaseModel):
    """
    Bracket Data

    Attributes:
        stage (Optional[BracketStage]): Bracket Stage
        group (List[BracketGroup]): Bracket Groups
        round (List[BracketRound]): Bracket Rounds
        match (List[BracketMatch]): Bracket Matches
    """
    stage: Optional[BracketStage]
    group: List[BracketGroup]
    round: List[BracketRound]
    match: List[BracketMatch]

    def __init__(self, data: dict, request_client: RequestsClient):
        super().__init__(data, request_client)
        stage = data.get("stage", [])
        self.stage = BracketStage(stage[0]) if len(stage) > 0 else None
        self.group = [BracketGroup(group) for group in data.get("group", [])]
        self.round = [BracketRound(r) for r in data.get("round", [])]
        self.match = [BracketMatch(match, request_client) for match in data.get("match", [])]


class Bracket(BaseModel):
    """
    Sendou.ink Tournament Bracket Info

    Attributes:
        data (BracketData): Bracket Data
        meta (BracketMeta): Bracket Metadata
    """
    data: BracketData  # https://github.com/Sendouc/sendou.ink/blob/rewrite/app/features/api-public/schema.ts#L232
    meta: BracketMeta

    def __init__(self, data: dict, request_client: RequestsClient):
        super().__init__(data, request_client)
        self.data = BracketData(data.get("data", {}), request_client)
        self.meta = BracketMeta(data.get("meta", {}))

    @staticmethod
    def api_route(**kwargs) -> str:
        """
        Get the api route for the bracket

        Args:
            tournament_id (str): Tournament ID
            bracket_index (int): Bracket Index

        Returns:
            (str): API Route
        """
        return f"api/tournament/{kwargs.get('tournament_id')}/brackets/{kwargs.get('bracket_index')}"
