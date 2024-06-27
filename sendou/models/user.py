"""
User Schema
"""
from .baseModel import BaseModel

from typing import List, Optional

from .plusServer import PlusTiers
from .badge import Badge
from sendou.requests import RequestsClient


class UserSocials:
    twitch: Optional[str]
    twitter: Optional[str]

    def __init__(self, data: dict):
        self.twitch = data.get("twitch")
        self.twitter = data.get("twitter")


class UserWeapon:
    id: str
    name: str
    is_five_star: bool

    def __init__(self, data: dict):
        self.id = str(data.get("id"))
        self.name = str(data.get("name"))
        self.is_five_star = bool(data.get("isFiveStar"))


class User(BaseModel):
    """
    GET /api/user/{userId|discordId}
    """
    id: int
    name: str
    discord_id: str
    url: str
    avatar_url: Optional[str]
    country: Optional[str]
    socials: UserSocials
    plus_server_tier: PlusTiers
    peak_xp: Optional[float]
    weapon_pool: List[UserWeapon]
    badges: List[Badge]

    def __init__(self, data: dict, request_client: RequestsClient):
        super().__init__(data, request_client)
        self.id = data.get("id", 0)
        self.name = str(data.get("name"))
        self.discord_id = str(data.get("discordId"))
        self.url = str(data.get("url"))
        self.avatar_url = data.get("avatarUrl", None)
        self.country = data.get("country", None)
        socials = data.get("socials", {})
        if socials:
            self.socials = UserSocials(socials)
        plus_server_tier = data.get("plusServerTier")
        if plus_server_tier:
            self.plus_server_tier = PlusTiers(plus_server_tier)
        self.peak_xp = data.get("peakXp", None)
        self.weapon_pool = [UserWeapon(weapon) for weapon in data.get("weaponPool", [])]
        self.badges = [Badge(badge) for badge in data.get("badges", [])]

    @staticmethod
    def api_route(**kwargs) -> str:
        """
        :param kwargs:
        :Keyword Arguments:
            user_id: str
        :return:
        """
        return f"api/user/{kwargs.get('user_id')}"


