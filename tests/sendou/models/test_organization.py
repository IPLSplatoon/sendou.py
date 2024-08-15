from sendou.models.organization import Organization, OrganizationMember, OrganizationRole
from sendou.requests import RequestsClient
from unittest.mock import MagicMock

def test_organization_model():
    data = {
        "id": 1,
        "name": "Test Organization",
        "description": "This is a test organization",
        "url": "https://sendou.ink/org/test",
        "logoUrl":"https://cdn.sendou.ink/org/inkling-performance-labs",
        "socialLinkUrls": ["https://x.com/IPLSplatoon"],
        "members": [
            {
                "userId": 1,
                "name": "Test User",
                "discordId": "211187184001231608",
                "role": "member",
                "roleDisplayName": "display_name"
            }
        ]
    }
    organization = Organization.from_dict(data, MagicMock(RequestsClient))
    assert organization.id == 1
    assert organization.name == "Test Organization"
    assert organization.description == "This is a test organization"
    assert organization.url == "https://sendou.ink/org/test"
    assert organization.logo_url == "https://cdn.sendou.ink/org/inkling-performance-labs"
    assert organization.social_link_urls == ["https://x.com/IPLSplatoon"]
    assert len(organization.members) == 1
    assert organization.members[0].user_id == 1
    assert organization.members[0].name == "Test User"
    assert organization.members[0].role == OrganizationRole.MEMBER
    assert organization.members[0].discord_id == "211187184001231608"
    assert organization.members[0].role_display_name == "display_name"

def test_organization_member_model():
    data = {
        "userId": 1,
        "name": "Test User",
        "discordId": "211187184001231608",
        "role": "member",
        "roleDisplayName": "display_name"
    }
    member = OrganizationMember.from_dict(data, MagicMock(RequestsClient))
    assert member.user_id == 1
    assert member.name == "Test User"
    assert member.role == OrganizationRole.MEMBER
    assert member.discord_id == "211187184001231608"
    assert member.role_display_name == "display_name"

def test_organization_role_model():
    assert OrganizationRole.MEMBER.value == "member"
    assert OrganizationRole.ADMIN.value == "admin"
    assert OrganizationRole.ORGANIZER.value == "organizer"
    assert OrganizationRole.STREAMER.value == "streamer"