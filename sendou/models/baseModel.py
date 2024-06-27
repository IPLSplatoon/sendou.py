"""
Base Model that routes inherit from
"""
from typing import Any, Dict, List, Union
from ..requests import RequestsClient


class BaseModel:
    _raw: Union[Dict[str, Any], List[Any], Any]  # Holes raw response from API
    _request_client: RequestsClient

    def __init__(self, data: Union[Dict[str, Any], List[Any]], request_client: RequestsClient):
        self._raw = data
        self._request_client = request_client

    @staticmethod
    def api_route(**kwargs) -> str:
        raise NotImplementedError("api_route not implemented")
