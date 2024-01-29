"""
User Schema
"""
from typing import List, Optional

from .plusServer import PlusTiers
from .badge import Badge


class UserSocials:
    twitch: Optional[str]
    twitter: Optional[str]


class UserWeapon:
    id: str
    name: str
    is_five_star: bool


class User:
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

