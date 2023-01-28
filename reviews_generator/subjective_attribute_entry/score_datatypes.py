from dataclasses import dataclass
from enum import Enum
from typing import Any
from abc import ABC


@dataclass
class Score:
    _score: float

    @property
    def score(self) -> float:
        return self._score

    @score.setter
    def score(self, given_score: float) -> None:
        if 10 < given_score < 0:
            raise ValueError('Numerical score must be between 0 and 10')
        self._score = given_score


class NarrativeScoreEnum(Enum):
    NA: "N/A"
    LORE: "Lore"
    TRADITIONAL: "Traditional Narrative"


@dataclass 
class NarrativeScore(Score):
    narrative_score_type: NarrativeScoreEnum


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
    score: GraphicalScoreEnum

@dataclass
class ScoringAttributes:
    total_score: Score
    narrative_score: NarrativeScore
    gameplay_score: Score
    graphics_score: GraphicalScore
