"""
Stage Info
"""
from enum import Enum


class ModeShort(Enum):
    TW = "TW"
    SZ = "SZ"
    TC = "TC"
    RM = "RM"
    CB = "CB"


class Stage:
    id: int
    name: str

    def __init__(self, data: dict):
        self.id = data.get("id")
        self.name = data.get("name")


class StageWithMode:
    mode: ModeShort
    stage: Stage

    def __init__(self, data: dict):
        self.mode = ModeShort(data.get("mode"))
        self.stage = Stage(data.get("stage"))
