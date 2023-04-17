from subjective_attribute_entry.score_datatypes import ScoringAttributes, NarrativeScoreEnum, GraphicalScoreEnum
from subjective_attribute_entry.play_datatypes import PlayAttributes, PreferredCoOpEnum


class SubjectiveAttributesBuilder:

    def __init__(self, video_game_name):
        self._scoring_attributes = ScoringAttributes()
        self._play_attributes = PlayAttributes()
    """
        Total Score (1.x-10; x=0-9)
    """

    def add_total_score(self, total_score: float) -> None:
        self._scoring_attributes.total_score = total_score

    """ 
        Narrative Ratings
            - N/A
            - Lore (1.x-10; x=0.9)
            - Traditional Narrative (1.x-10; x=0-9)
    """

    def add_narrative_score(self, narrative_type: NarrativeScoreEnum, narrative_score: float) -> None: 
        self._scoring_attributes.narrative_score = narrative_score 
        self._scoring_attributes.narrative_type = narrative_type

    """
        Gameplay Score (1.x-10; x=0-9)
    """

    def add_gameplay_score(self, gameplay_score: float) -> None:
        self._scoring_attributes.gameplay_score = gameplay_score

    """
        Graphics Ratings
            - Timeless
            - Artistically-Subjective 
            - At present accepted as excellent
            - At present accepted as good
            - Outdated at present but excellent on release
            - Outdated at present but good on release
            - Considered poor at the time of release
    """

    def add_graphics_score(self, graphics_type: GraphicalScoreEnum, graphics_score: float) -> None:
        self._scoring_attributes.gameplay_score = graphics_score
        self._scoring_attributes.graphics_type = graphics_type

    """
        The game is better played with friends if true.
        Preferred co-op type:
            - Online Multiplayer
            - Splitscreen
            - Controller Pass
            - Party Game
    """

    def add_estimated_play_date(self, estimated_play_date: str) -> None:
        self._play_attributes.estimated_play_date = estimated_play_date

    def add_completed(self, is_completed: bool) -> None:
        self._play_attributes.completed = is_completed

    def add_hours_played(self, hours_played: int) -> None:
        self._play_attributes.hours_played = hours_played

    def add_better_with_friends(self, is_better: bool) -> None:
        self._play_attributes.better_with_friends = is_better

    def add_preferred_co_op_type(self, preferred_co_op_type: PreferredCoOpEnum) -> None:
        self._play_attributes.preferred_co_op_type = preferred_co_op_type

    def add_recommend_the_ost(self, recommend_the_ost: bool) -> None:
        self._play_attributes.recommend_the_ost = recommend_the_ost




