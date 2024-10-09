from .baseModel import BaseModel
from sendou.requests import RequestsClient
from typing import Optional
from datetime import datetime
from dateutil import parser

from .tournament import Tournament


class CalendarEntry(BaseModel):
    """
    Calendar Entry Model

    Attributes:
        name (str): Event Name
        tournament_id (int): Tournament ID
        tournament_url (str): Tournament URL
        start_time (datetime): Event Start Time
    """
    name: str
    tournament_id: Optional[int]
    tournament_url: Optional[str]
    start_time: datetime

    def __init__(self, data: dict, request_client: RequestsClient):
        super().__init__(data, request_client)
        self.name = data.get("name", "")
        self.tournament_id = data.get("tournamentId", None)
        self.tournament_url = data.get("tournamentUrl", "")
        self.start_time = parser.parse(data.get("startTime", ""))

    @staticmethod
    def api_route(**kwargs) -> str:
        """
        API Route
        Args:
            year (int): Year
            week (int): week

        Returns:
            str: API Route
        """
        return f"api/calendar/{kwargs.get('year')}/{kwargs.get('week')}"

    async def get_tournament(self) -> Optional[Tournament]:
        """
        Get the tournament for the calendar entry
        Returns:
            (Optional[Tournament]): Tournament
        """
        if self.tournament_id is None:
            return None
        path = Tournament.api_route(tournament_id=self.tournament_id)
        data = await self._request_client.get_response(path)
        return Tournament(self.tournament_id, data, self._request_client)

    def __repr__(self):
        return f"<CalendarEntry name={self.name} | tournament_id={self.tournament_id} | start_time={self.start_time}>"
