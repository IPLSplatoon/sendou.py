"""
Tournament Bracket Model
"""
from sendou.models.baseModel import BaseModel
from sendou.requests import RequestsClient

from typing import Any, Optional


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


class Bracket(BaseModel):
    """
    Sendou.ink Tournament Bracket Info

    Attributes:
        data (Any): Bracket Data
        meta (BracketMeta): Bracket Metadata
    """
    data: Any  # https://github.com/Sendouc/sendou.ink/blob/rewrite/app/features/api-public/schema.ts#L232
    meta: BracketMeta

    def __init__(self, data: dict, request_client: RequestsClient):
        super().__init__(data, request_client)
        self.data = data.get("data", {})
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

