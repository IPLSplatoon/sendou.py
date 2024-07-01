from enum import Enum


class BracketType(Enum):
    """
    Bracket Types

    Values:
        SINGLE_ELIMINATION: Single Elimination Bracket
        DOUBLE_ELIMINATION: Double Elimination Bracket
        ROUND_ROBIN: Round Robin Bracket
        SWISS: Swiss Bracket
    """
    SINGLE_ELIMINATION = "single_elimination"
    DOUBLE_ELIMINATION = "double_elimination"
    ROUND_ROBIN = "round_robin"
    SWISS = "swiss"


class RoundType(Enum):
    """
    Round Types

    Values:
        BEST_OF: Best of round
        PLAY_ALL: Play all games
    """
    best_of = "BEST_OF"
    play_all = "PLAY_ALL"


class MatchResult(Enum):
    """
    Match Results

    Values:
        WIN: Win
        LOSS: Loss
        DRAW: Draw
    """
    WIN = "win"
    LOSS = "loss"
    DRAW = "draw"
