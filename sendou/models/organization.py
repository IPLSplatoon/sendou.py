"""
Org Model
"""
from sendou.models.baseModel import BaseModel
from sendou.requests import RequestsClient

from typing import Optional, List
from enum import Enum

from .user import User


class OrganizationRole(Enum):
    """
    Represents a role of member in the organization
    """
    ADMIN = "admin"
    MEMBER = "member"
    ORGANIZER = "organizer"
    STREAMER = "streamer"


class OrganizationMember(BaseModel):
    """
    Represents a member of the organization

    Attributes:
        user_id: User ID
        name: User name
        discord_id: Discord ID
        role: OrganizationRole
        role_display_name: Display name of the role
    """
    user_id: int
    name: str
    discord_id: str
    role: OrganizationRole
    role_display_name: Optional[str]

    def __init__(self, data: dict, request_client: RequestsClient):
        super().__init__(data, request_client)
        self.user_id = data.get("userId")
        self.name = data.get("name")
        self.discord_id = data.get("discordId")
        self.role = OrganizationRole(data.get("role"))
        self.role_display_name = data.get("roleDisplayName", None)

    async def get_user(self) -> Optional[User]:
        """
        Get the user object for this member

        Returns:
            (User): User object
        """
        path = User.api_route(user_id=self.user_id)
        data = await self._request_client.get_response(path)
        return User(data, self._request_client)


class Organization(BaseModel):
    """
    Represents an organization

    Attributes:
        id: Organization ID
        name: Organization name
        description: Organization description
        url: Organization URL
        logo_url: Organization logo URL
        social_link_urls: List of social link URLs
        members: List of OrganizationMember
    """
    id: int
    name: str
    description: Optional[str]
    url: str
    logo_url: Optional[str]
    social_link_urls: List[str]
    members: List[OrganizationMember]

    def __init__(self, data: dict, request_client: RequestsClient):
        super().__init__(data, request_client)
        self.id = data.get("id")
        self.name = data.get("name")
        self.description = data.get("description", None)
        self.url = data.get("url")
        self.logo_url = data.get("logoUrl", None)
        self.social_link_urls = data.get("socialLinkUrls")
        self.members = [OrganizationMember(member, request_client) for member in data.get("members")]

