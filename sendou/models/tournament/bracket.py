"""
Tournament Bracket Model
"""
from sendou.models.baseModel import BaseModel
from sendou.requests import RequestsClient

from datetime import datetime
from dateutil import parser
from typing import Any, Dict, List, Optional
from enum import Enum


class BracketMeta:
    teams_per_group: Optional[int]
    group_count: Optional[int]
    round_count: Optional[int]

    def __init__(self, data: dict):
        self.teams_per_group = data.get("teamsPerGroup", None)
        self.group_count = data.get("groupCount", None)
        self.round_count = data.get("roundCount", None)


class Bracket(BaseModel):
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
        :param kwargs:
        :Keyword Arguments:
            tournament_id: str
            bracket_index: int
        :return:
        """
        return f"api/tournament/{kwargs.get('tournament_id')}/brackets/{kwargs.get('bracket_index')}"

