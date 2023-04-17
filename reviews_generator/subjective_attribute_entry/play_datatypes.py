from dataclasses import dataclass
from enum import Enum


class PreferredCoOpEnum:
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
    _preferred_co_op_type: PreferredCoOpEnum
    recommend_the_ost: bool 

    @property
    def preferred_co_op_type(self) -> str:
        return self._preferred_co_op_type.value

    @preferred_co_op_type.setter
    def preferred_co_op_type(self, given_preferred_co_op_type: PreferredCoOpEnum) -> None:
        self._preferred_co_op_type = given_preferred_co_op_type