from enum import auto
from enum import Enum
from enum import IntFlag


class Hand(IntFlag):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


class Result(Enum):
    WIN = auto()
    LOSE = auto()
    DRAW = auto()
