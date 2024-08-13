"""
Models for "official" api
Based off of https://github.com/Sendouc/sendou.ink/blob/rewrite/app/features/api-public/schema.ts#L114
"""
from .tournament import *
from .user import User, UserWeapon, UserSocials
from .badge import Badge
from .plusServer import PlusTiers
from .stageMapList import Stage, ModeShort, StageWithMode
from .calendarEntry import CalendarEntry
from .organization import Organization
