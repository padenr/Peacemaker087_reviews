from dataclasses import dataclass


@dataclass
class WikipediaEntry:
    title: str = None
    developers: list = None
    directors: list = None
    publishers: list = None
    composers: list = None
    series: str = None
    platforms: list = None
    release_data: str = None
    genres: list = None
    image_url: str = None

    def format_as_json(self) -> dict:
        wikipedia_entry_json = {
            "title": self.title,
            "developers": self.developers,
            "directors": self.directors,
            "publishers": self.publishers,
            "composers": self.composers,
            "series": self.series,
            "platforms": self.platforms,
            "release_data": self.release_data,
            "genres": self.genres,
        }
        return wikipedia_entry_json 


@dataclass 
class MetacriticEntry:
    metascore: float = -1
    user_score: float = -1
    rating: str = None

    def format_as_json(self) -> dict:
        metacritic_entry_json = {
            "metascore": self.metascore,
            "user_score": self.user_score,
            "rating": self.rating
        }
        return metacritic_entry_json