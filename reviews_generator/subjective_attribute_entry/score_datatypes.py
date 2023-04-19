from dataclasses import dataclass
from enum import Enum


@dataclass
class Score:
    _score: float = -1

    @property
    def score(self) -> float:
        return self._score

    @score.setter
    def score(self, given_score: float) -> None:
        if not 0 <= given_score <= 10:
            raise ValueError('Numerical score must be between 0 and 10')
        self._score = given_score


class NarrativeScoreEnum(Enum):
    NA: "N/A"
    LORE: "Lore"
    TRADITIONAL: "Traditional Narrative"


@dataclass 
class NarrativeScore(Score):
    _narrative_score_type: NarrativeScoreEnum = None

    @property 
    def narrative_type(self) -> str:
        return self._narrative_score_type.value
    
    @narrative_type.setter
    def narrative_score_type(self, given_narrative_type: NarrativeScoreEnum) -> None:
        self._narrative_type = given_narrative_type


class GraphicalScoreEnum(Enum):
    TIMELESS: "Timeless"
    ART_SUBJECTIVE: "Artistically subjective"
    MODERN_EXCELLENT: "Modern example of a graphically excellent game"
    MODERN_GOOD: "Modern example of a graphically good game"
    MODERN_MEDIOCRE: "Modern example of a graphically mediocre game"
    OUTDATED_EXCELLENT: "Outdated by modern standards but excellent on release"
    OUTDATED_GOOD: "Outdated by modern standards but good on release"
    OUTDATED_MEDIOCRE: "Outdated by modern standards but mediocre on release"
    POOR_ON_RELEASE: "Poor when the game released"


@dataclass
class GraphicalScore(Score):
    score: GraphicalScoreEnum = None

    @property
    def graphical_score_type(self) -> str:
        return self._graphical_score_type.value
    
    @graphical_score_type.setter
    def graphical_score_type(self, given_graphical_score_type: GraphicalScoreEnum) -> None:
        self._graphical_score_type = given_graphical_score_type


class ScoringAttributes:
    
    def __init__(self):
        self._total_score: Score = None
        self._narrative_score: NarrativeScore = None
        self._gameplay_score: Score = None
        self._graphics_score: GraphicalScore = None

    @property
    def total_score(self) -> float:
        return self._total_score.score
    
    @total_score.setter
    def total_score(self, given_total_score: float) -> None:
        self._total_score = Score()
        self._total_score.score = given_total_score

    @property
    def narrative_score(self) -> float:
        return self._narrative_score.score
    
    @narrative_score.setter
    def narrative_score(self, given_narrative_score: float) -> None:
        self._narrative_score = NarrativeScore()
        self._narrative_score.score = given_narrative_score
    
    @property
    def narrative_type(self) -> str:
        return self._narrative_score.narrative_type
    
    @narrative_type.setter
    def narrative_type(self, given_narrative_type: NarrativeScoreEnum) -> None:
        self._narrative_score.narrative_type = given_narrative_type
    
    @property
    def gameplay_score(self) -> float:
        return self._gameplay_score.score

    @property
    def graphical_score(self) -> float:
        return self._graphical_score.score
    
    @graphical_score.setter
    def graphical_score(self, given_graphical_score: float) -> None:
        self._graphical_score = GraphicalScore()
        self._graphical_score.score = given_graphical_score
    
    @property
    def graphical_type(self) -> str:
        return self._graphical_score.graphical_type
    
    @graphical_type.setter
    def graphical_type(self, given_graphical_type: GraphicalScoreEnum) -> None:
        self._graphical_score = GraphicalScore()
        self._graphical_score.graphical_type = given_graphical_type

    

