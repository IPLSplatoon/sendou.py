from aiohttp_client_cache import CacheBackend
from aiohttp_client_cache.session import CachedSession
from typing import Dict, Any


class RequestsClient:
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
    def create(cls, base_url: str, expiry: int = 1800, headers=None):
        cache = CacheBackend(expiry=expiry)
        return cls(base_url, cache, headers=headers)

    async def get_response(self, path: str) -> Any:
        async with CachedSession(cache=self.cache) as session:
            async with session.get(f"{self.base_url}/{path}", headers=self.__headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Failed to get response from {self.base_url}/{path}")
