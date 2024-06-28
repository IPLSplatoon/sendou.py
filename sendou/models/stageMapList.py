"""
Stage Info
"""
from enum import Enum


class ModeShort(Enum):
    """
    Splatoon Game Mode Shorthands

    Values:
        TW: Turf War,
        SZ: Splat Zones,
        TC: Tower Control,
        RM: Rainmaker,
        CB: Clam Blitz
    """
    TW = "TW"  # Turf War
    SZ = "SZ"  # Splat Zones
    TC = "TC"  # Tower Control
    RM = "RM"  # Rainmaker
    CB = "CB"  # Clam Blitz


class Stage:
    """
    Team Map Pool Stage

    Attributes:
        id (int): Stage ID
        name (str): Stage Name
    """
    id: int
    name: str

    def __init__(self, data: dict):
        self.id = data.get("id", 0)
        self.name = data.get("name", "")


class StageWithMode:
    """
    Stage & Mode Info

    Attributes:
        mode (ModeShort): Game Mode
        stage (Stage): Stage
    """
    mode: ModeShort
    stage: Stage

    def __init__(self, data: dict):
        self.mode = ModeShort(data.get("mode"))
        self.stage = Stage(data.get("stage", {}))
