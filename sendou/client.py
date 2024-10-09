from typing import Dict, List, Optional, Union
from datetime import datetime, timedelta
from aiohttp_client_cache import CacheBackend
from sendou.models import User, Tournament, Match, CalendarEntry, Organization
from sendou.requests import RequestsClient


class Client:
    """
    Sendou.ink Async API Client

    Attributes:
            api_key (str): Sendou.ink API Key
            headers (Dict[str, str]): Custom Headers
            url (str): Sendou.ink URL (**Default:** https://sendou.ink)
            expiry (Union[None, int, float, str, datetime, timedelta]): Cache Expiry Time (**Default:** 1800)

    Examples:
        ```python
        from sendou import Client

        client = Client("API")
        ```
    """
    __header: Dict[str, str]
    __client: RequestsClient

    def __init__(self, api_key: str, headers: Dict[str, str] = {}, url: Optional[str] = None,
                 expiry: Union[None, int, float, str, datetime, timedelta] = 1800):
        self.__headers = headers
        if "User-Agent" not in self.__headers:
            self.__headers["User-Agent"] = "sendou.py"
        if url:
            self.url = url
        else:
            self.url = "https://sendou.ink"
        self.__headers["Authorization"] = f"Bearer {api_key}"
        self.__client = RequestsClient.create(self.url, headers=self.__headers, expiry=expiry)

    def set_cache_backend(self, cache: CacheBackend):
        """
        Set the cache backend for the client. Use if you want to use a custom cache backend.

        Attributes:
            cache: Cache Backend

        Returns:
            (None): None
        """
        self.__client.cache = cache

    async def get_user(self, user_id: str) -> Optional[User]:
        """
        Get Sendou.ink user

        Attributes:
            user_id: User ID

        Returns:
            (Optional[User]): User (None if not found)

        Examples:
            ```python
            import sendou
            import asyncio

            async def run():
                client = sendou.Client("API_KEY")
                player = await client.get_user("USER_ID")
                print(player.name)

            asyncio.run(run())
            ```
        """
        path = User.api_route(user_id=user_id)
        data = await self.__client.get_response(path)
        return User(data, self.__client)

    async def get_calendar(self, year: int, week: int) -> List[CalendarEntry]:
        """
        Get Sendou.ink calendar

        Attributes:
            year: Year
            week: Week of year

        Returns:
            (List[CalendarEntry]): Calendar Entries
        """
        path = CalendarEntry.api_route(year=year, week=week)
        data = await self.__client.get_response(path)
        return [CalendarEntry(entry, self.__client) for entry in data]

    async def get_tournament(self, tournament_id: str) -> Optional[Tournament]:
        """
        Get Sendou.ink tournament

        Attributes:
            tournament_id: Tournament ID

        Returns:
            (Optional[Tournament]): Tournament (None if not found)
        """
        path = Tournament.api_route(tournament_id=tournament_id)
        data = await self.__client.get_response(path)
        return Tournament(int(tournament_id), data, self.__client)

    async def get_tournament_matches(self, match_id: str) -> Optional[Match]:
        """
        Get Sendou.ink match

        Attributes:
            match_id: Match ID

        Returns:
            (Optional[Match]): Match (None if not found)
        """
        path = Match.api_route(match_id=match_id)
        data = await self.__client.get_response(path)
        return Match(data, self.__client)

    async def get_organization(self, organization_id: str) -> Optional[Organization]:
        """
        Get Sendou.ink organization

        Attributes:
            organization_id: Organization ID

        Returns:
            (Optional[Organization]): Organization (None if not found)
        """
        path = Organization.api_route(organization_id=organization_id)
        data = await self.__client.get_response(path)
        return Organization.from_dict(data, self.__client)
