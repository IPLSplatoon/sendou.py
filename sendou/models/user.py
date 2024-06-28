"""
User Schema
"""
from .baseModel import BaseModel

from typing import List, Optional

from .plusServer import PlusTiers
from .badge import Badge
from sendou.requests import RequestsClient


class UserSocials:
    """
    User Socials Accounts

    Attributes:
        twitch (Optional[str]): Twitch Username
        twitter (Optional[str]): Twitter Username
    """
    twitch: Optional[str]
    twitter: Optional[str]

    def __init__(self, data: dict):
        self.twitch = data.get("twitch")
        self.twitter = data.get("twitter")


class UserWeapon:
    """
    User Weapon in Weapon pool

    Attributes:
        id (str): Weapon ID
        name (str): Weapon Name
        is_five_star (bool): Is Five Star Weapon
    """
    id: str
    name: str
    is_five_star: bool

    def __init__(self, data: dict):
        self.id = str(data.get("id"))
        self.name = str(data.get("name"))
        self.is_five_star = bool(data.get("isFiveStar"))


class User(BaseModel):
    """
    Sendou.ink User

    Attributes:
        id (int): User ID
        name (str): User Name
        discord_id (str): Discord ID
        url (str): User URL
        avatar_url (Optional[str]): Avatar URL
        country (Optional[str]): Country
        socials (UserSocials): Socials
        plus_server_tier (Optional[PlusTiers]): Plus Server Tier
        peak_xp (Optional[float]): Peak XP
        weapon_pool (List[UserWeapon]): Weapon Pool
        badges (List[Badge]): Badges
    """
    id: int
    name: str
    discord_id: str
    url: str
    avatar_url: Optional[str]
    country: Optional[str]
    socials: UserSocials
    plus_server_tier: Optional[PlusTiers]
    peak_xp: Optional[float]
    weapon_pool: List[UserWeapon]
    badges: List[Badge]

    def __init__(self, data: dict, request_client: RequestsClient):
        """
        Init
        :param data: Raw data from API
        :type data: dict
        :param request_client: Request Client
        :type request_client: RequestsClient
        """
        super().__init__(data, request_client)
        self.id = data.get("id", 0)
        self.name = str(data.get("name"))
        self.discord_id = str(data.get("discordId"))
        self.url = str(data.get("url"))
        self.avatar_url = data.get("avatarUrl", None)
        self.country = data.get("country", None)
        self.socials = UserSocials(data.get("socials", {}))
        self.plus_server_tier = None
        plus_server_tier = data.get("plusServerTier")
        if plus_server_tier:
            self.plus_server_tier = PlusTiers(plus_server_tier)
        self.peak_xp = data.get("peakXp", None)
        self.weapon_pool = [UserWeapon(weapon) for weapon in data.get("weaponPool", [])]
        self.badges = [Badge(badge) for badge in data.get("badges", [])]

    @staticmethod
    def api_route(**kwargs) -> str:
        """
        Returns API route for the model

        Args:
            user_id (str): User ID

        Returns:
            (str): API Route
        """
        return f"api/user/{kwargs.get('user_id')}"


