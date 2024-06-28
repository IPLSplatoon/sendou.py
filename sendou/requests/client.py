from aiohttp_client_cache import CacheBackend
from aiohttp_client_cache.session import CachedSession
from typing import Dict, Any


class RequestsClient:
    """A simple wrapper around aiohttp_client_cache to make requests to a base_url with caching."""
    base_url: str
    cache: CacheBackend
    __headers: Dict[str, str]

    def __init__(self, base_url: str, cache: CacheBackend, headers=None):
        """
        Init
        :param base_url: Base URL for the requests
        :param cache: CacheBackend object
        :param headers: Headers to be sent with the requests
        """
        self.base_url = base_url
        if headers is None:
            self.__headers = {}
        else:
            self.__headers = headers
        self.cache = cache

    @classmethod
    def create(cls, base_url: str, expiry: int = 1800, headers=None):
        """
        Create a new RequestsClient object with basic Cache Backend
        :param base_url: Base URL for the requests
        :param expiry: Expiry time for the cache (Seconds)
        :param headers: User defined headers
        :return: RequestsClient object
        """
        cache = CacheBackend(expiry=expiry)
        return cls(base_url, cache, headers=headers)

    async def get_response(self, path: str) -> Any:
        """
        Get response from the base_url/path
        :param path: Path to get the response from
        :return: JSON response
        """
        async with CachedSession(cache=self.cache) as session:
            async with session.get(f"{self.base_url}/{path}", headers=self.__headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Failed to get response from {self.base_url}/{path}")