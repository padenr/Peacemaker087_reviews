from dataclasses import dataclass


@dataclass
class GameMetadata:
    title: str
    series: str
    director: str
    publishers: str
    platforms: []
    release_data: str
    genres: []


class ThirdPartyReviews:
    metacritic_audience: float
    metacritic_critic: float
    ign: float
    polygon: float
    gamespot: float
    pc_gamer: float