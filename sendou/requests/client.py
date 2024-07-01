from aiohttp_client_cache import CacheBackend
from aiohttp_client_cache.session import CachedSession
from typing import Dict, Any, Union
from datetime import datetime, timedelta


class RequestsClient:
    """
    A simple wrapper around aiohttp_client_cache to make requests to a base_url with caching.

    Args:
        base_url: Base URL for the requests
        cache: Cache Backend
        headers: User defined headers

    Examples:
        ```python
        from aiohttp_client_cache import CacheBackend
        from sendou.requests import RequestsClient

        cache = CacheBackend()
        client = RequestsClient("https://sendou.ink", cache)
        ```
    """
    base_url: str
    cache: CacheBackend
    __headers: Dict[str, str]

    def __init__(self, base_url: str, cache: CacheBackend, headers=None):
        self.base_url = base_url
        if headers is None:
            self.__headers = {}
        else:
            self.__headers = headers
        self.cache = cache

    @classmethod
    def create(cls, base_url: str, expiry: Union[None, int, float, str, datetime, timedelta] = 1800, headers=None):
        """
        Create a new RequestsClient object with basic Cache Backend

        Args:
            base_url: Base URL for the requests
            expiry: Expiry time for the cache
            headers: User defined headers

        Returns:
            (RequestsClient): New RequestsClient object

        Examples:
            ```python
            from aiohttp_client_cache import CacheBackend
            from sendou.requests import RequestsClient

            client = RequestsClient.create("https://sendou.ink")
            ```
        """
        cache = CacheBackend(expiry=expiry)
        return cls(base_url, cache, headers=headers)

    async def get_response(self, path: str) -> Any:
        """
        Get response from the base_url/path

        Args:
            path: Path to get the response from

        Returns:
            (Any): Response data
        """
        async with CachedSession(cache=self.cache) as session:
            async with session.get(f"{self.base_url}/{path}", headers=self.__headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Failed to get response from {self.base_url}/{path}")
