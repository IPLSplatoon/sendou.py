"""
User Schema
"""
from typing import List, Optional

from .plusServer import PlusTiers
from .badge import Badge


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
        self.id = data.get("id")
        self.name = data.get("name")
        self.is_five_star = data.get("isFiveStar")


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

    def __init__(self, data: dict):
        self.id = data.get("id")
        self.name = data.get("name")
        self.discord_id = data.get("discordId")
        self.url = data.get("url")
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


