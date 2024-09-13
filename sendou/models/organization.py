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
    admin = "ADMIN"
    member = "MEMBER"
    organizer = "ORGANIZER"
    streamer = "STREAMER"


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

    def __init__(self, data: dict, user_id: int, name: str, discord_id: str, role: OrganizationRole,
                 role_display_name: Optional[str], request_client: RequestsClient):
        super().__init__(data, request_client)
        self.user_id = user_id
        self.name = name
        self.discord_id = discord_id
        self.role = role
        self.role_display_name = role_display_name

    @classmethod
    def from_dict(cls, data: dict, request_client: RequestsClient):
        user_id = data.get("userId")
        name = data.get("name")
        discord_id = data.get("discordId")
        role = OrganizationRole(data.get("role"))
        role_display_name = data.get("roleDisplayName", None)
        return cls(data, user_id, name, discord_id, role, role_display_name, request_client)


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

    def __init__(self, data: dict, id: int, name: str, description: Optional[str], url: str, logo_url: Optional[str],
                 social_link_urls: List[str], members: List[OrganizationMember], request_client: RequestsClient):
        super().__init__(data, request_client)
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.logo_url = logo_url
        self.social_link_urls = social_link_urls
        self.members = members

    @classmethod
    def from_dict(cls, data: dict, request_client: RequestsClient):
        id = data.get("id")
        name = data.get("name")
        description = data.get("description", None)
        url = data.get("url")
        logo_url = data.get("logoUrl", None)
        social_link_urls = data.get("socialLinkUrls")
        members = [OrganizationMember.from_dict(member, request_client) for member in data.get("members")]
        return cls(data, id, name, description, url, logo_url, social_link_urls, members, request_client)

    @staticmethod
    def api_route(**kwargs) -> str:

        """
        Get the API route for organizations

        Kwargs:
            org_id: Organization ID

        Returns:
            (str): API route
        """
        return f"api/org/{kwargs.get('org_id')}"

