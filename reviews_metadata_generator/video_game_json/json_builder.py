import json

from reviews_metadata_generator.subjective_attribute_entry.play_data_types import PlayAttributes
from reviews_metadata_generator.subjective_attribute_entry.score_data_types import SubjectiveScoringAttributes

from reviews_metadata_generator.data_scraping.game_metadata_datatypes import WikipediaEntry, MetacriticEntry


class JSONBuilder:

    def __init__(self):
        self.__video_game_json = {}

    def add_play_data(self, play_attributes: PlayAttributes) -> None:
        self.__video_game_json['play_attributes'] = play_attributes.format_as_json()

    def add_wikipedia_data(self, wikipedia_entry: WikipediaEntry) -> None:
        self.__video_game_json['wikipedia_entry'] = wikipedia_entry.format_as_json()

    def add_metacritic_data(self, metacritic_entry: MetacriticEntry) -> None:
        self.__video_game_json['metacritic_entry'] = metacritic_entry.format_as_json()

    def add_subjective_scoring_data(self, subjective_scoring_attributes: SubjectiveScoringAttributes) -> None:
        self.__video_game_json['subjective_scoring_attributes'] = subjective_scoring_attributes.format_as_json()

    def write_json(self, json_file_path: str):
        with open(json_file_path, 'w') as json_file_handle:
            json.dump(self.__video_game_json, json_file_handle, indent=4)