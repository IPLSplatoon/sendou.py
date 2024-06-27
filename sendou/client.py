from typing import Dict, List, Optional
from aiohttp_client_cache import CacheBackend
from .models import User, Tournament, Match
from .requests import RequestsClient


class Client:
    __header: Dict[str, str]
    __client: RequestsClient

    def __init__(self, api_key: str, headers: Dict[str, str] = {}, url: Optional[str] = None):
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
        Set the cache backend for the client
        :param cache:
        :return: None
        """
        self.__client.cache = cache

    async def get_user(self, user_id: str) -> Optional[User]:
        """
        Get Sendou.ink user
        :param user_id:
        :return:
        """
        path = User.api_route(user_id=user_id)
        data = await self.__client.get_response(path)
        return User(data, self.__client)

    async def get_tournament(self, tournament_id: str) -> Optional[Tournament]:
        """
        Get a list of tournaments
        :param tournament_id:
        :return: List of Tournaments
        """
        path = Tournament.api_route(tournament_id=tournament_id)
        data = await self.__client.get_response(path)
        return Tournament(tournament_id, data, self.__client)

    async def get_tournament_matches(self, tournament_id: str) -> Optional[List[Match]]:
        """
        Get a list of tournament matches
        :param tournament_id:
        :return: List of Matches
        """
        path = Match.api_route(tournament_id=tournament_id)
        data = await self.__client.get_response(path)
        return [Match(match, self.__client) for match in data]

