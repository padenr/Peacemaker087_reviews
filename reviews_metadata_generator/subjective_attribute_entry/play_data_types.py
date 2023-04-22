from dataclasses import dataclass
from enum import Enum

from reviews_metadata_generator.data_types import Date


class PreferredCoOpEnum(Enum):
    NA = "N/A"
    MULTIPLAYER = "Online multiplayer"
    SPLITSCREEN = "Splitscreen"
    CONTROLLER_PASS = "Pass around the controller"
    PARTY_GAME = "Party game"

class PlatformEnum(Enum):
    SWITCH = "Nintendo Switch"
    PS4 = "PlayStation 4"


@dataclass
class PlayAttributes:
    estimated_play_date: Date = None
    completed: bool = False
    better_with_friends: bool = False
    recommend_the_ost: bool  = False
    _hours_played: int = -1
    _platform: PlatformEnum = None
    _preferred_co_op_type: PreferredCoOpEnum = None

    @property
    def platform(self) -> str:
        return self._platform.value
    
    @platform.setter
    def platform(self, given_platform: PlatformEnum) -> None:
        self._platform = given_platform

    @property
    def preferred_co_op_type(self) -> str:
        return self._preferred_co_op_type.value

    @preferred_co_op_type.setter
    def preferred_co_op_type(self, given_preferred_co_op_type: PreferredCoOpEnum) -> None:
        self._preferred_co_op_type = given_preferred_co_op_type

    @property
    def hours_played(self) -> int:
        return self._hours_played
    
    @hours_played.setter
    def hours_played(self, given_hours_played: int) -> None:
        if given_hours_played < 0:
            raise ValueError("Hours played must be a positive integer.")
        self._hours_played = given_hours_played

    def format_as_json(self) -> dict:
        play_attributes_json = {
            "estimated_play_date": str(self.estimated_play_date),
            "platform": self.platform,
            "completed": self.completed,
            "hours_played": self.hours_played,
            "better_with_friends": self.better_with_friends,
            "preferred_co_op_type": self.preferred_co_op_type,
            "recommend_the_ost": self.recommend_the_ost
        }
        return play_attributes_json