"""
Stage Info
"""
from enum import Enum


class ModeShort(Enum):
    TW = "tw"
    SZ = "sz"
    TC = "tc"
    RM = "rm"
    CB = "cb"


class Stage:
    id: int
    name: str


class StageWithMode:
    mode: ModeShort
    stage: Stage
