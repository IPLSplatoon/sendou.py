"""
Base Model that routes inherit from
"""
from typing import Any, Dict, List, Union
from ..requests import RequestsClient


class BaseModel:
    """
    base model for all the models

    Attributes:
        _raw (Union[Dict[str, Any], List[Any], Any]): Raw response from API
        _request_client (RequestsClient): Request Client
    """
    _raw: Union[Dict[str, Any], List[Any], Any]  # Holes raw response from API
    _request_client: RequestsClient

    def __init__(self, data: Union[Dict[str, Any], List[Any]], request_client: RequestsClient):
        """
        Init

        Args:
            data: Raw data from API
            request_client: Request Client
        """
        self._raw = data
        self._request_client = request_client

    @staticmethod
    def api_route(**kwargs) -> str:
        """Returns API route for the model (Not Implemented in BaseModel)"""
        raise NotImplementedError("api_route not implemented")
