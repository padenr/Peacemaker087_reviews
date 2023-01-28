from dataclasses import dataclass
from enum import Enum


class PreferredCoOpType:
    NA: "N/A"
    MULTIPLAYER: "Online multiplayer"
    SPLITSCREEN: "Splitscreen"
    CONTROLLER_PASS: "Pass around the controller"
    PARTY_GAME: "Party game"


@dataclass
class PlayAttributes:
    estimated_play_date: str
    completed: bool
    hours_played: int
    better_with_friends: bool
    preferred_co_op_type: PreferredCoOpType
    recommend_the_ost: bool 
