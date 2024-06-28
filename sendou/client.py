from typing import Dict, List, Optional
from aiohttp_client_cache import CacheBackend
from sendou.models import User, Tournament, Match
from sendou.requests import RequestsClient


class Client:
    """
    Sendou.ink Async API Client
    """
    __header: Dict[str, str]
    __client: RequestsClient

    def __init__(self, api_key: str, headers: Dict[str, str] = {}, url: Optional[str] = None):
        """
        Init

        Attributes:
            api_key (str): Sendou.ink API Key
            headers (Dict[str, str]): Custom Headers
            url (str): Sendou.ink URL (**Default:** https://sendou.ink)

        Returns:
            (None): None
        """
        self.__headers = headers
        if "User-Agent" not in self.__headers:
            self.__headers["User-Agent"] = "sendou.py"
        if url:
            self.url = url
        else:
            self.url = "https://sendou.ink"
        self.__headers["Authorization"] = f"Bearer {api_key}"
        self.__client = RequestsClient.create(self.url, headers=self.__headers)

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
            (Optional[User]): User (None if not found
        """
        path = User.api_route(user_id=user_id)
        data = await self.__client.get_response(path)
        return User(data, self.__client)

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
        return Tournament(tournament_id, data, self.__client)

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

