import os 

from reviews_metadata_generator.data_scraping.api import ScrapingAPI
from reviews_metadata_generator.data_scraping.data_scraper import MetacriticConsoleEnum
from reviews_metadata_generator.subjective_attribute_entry.subjective_attributes_builder import SubjectiveAttributesBuilder

from reviews_metadata_generator.subjective_attribute_entry.play_data_types import PreferredCoOpEnum, PlatformEnum
from reviews_metadata_generator.subjective_attribute_entry.score_data_types import GraphicalScoreEnum, NarrativeScoreEnum

from reviews_metadata_generator.video_game_json.json_builder import JSONBuilder
from reviews_metadata_generator.online_image_saver import OnlineImageSaver

REVIEWS_DIRECTORY = "G:\\My Drive\\video_game_reviews\\vg_json"
COVER_ART_DIRECTORY = "G:\\My Drive\\video_game_reviews\\vg_cover_art"


def __main__():
    subjective_attributes_builder = SubjectiveAttributesBuilder()
    subjective_attributes_builder.add_total_score(9.5)
    subjective_attributes_builder.add_narrative_score(NarrativeScoreEnum.LORE, 9.5)
    subjective_attributes_builder.add_gameplay_score(9.5)
    subjective_attributes_builder.add_graphical_score(GraphicalScoreEnum.MODERN_GOOD, 9.5)
    subjective_attributes_builder.add_estimated_play_date("2020-01-01")
    subjective_attributes_builder.add_hours_played(100)
    subjective_attributes_builder.add_platform(PlatformEnum.SWITCH)
    subjective_attributes_builder.add_completed(True)
    subjective_attributes_builder.add_better_with_friends(True)
    subjective_attributes_builder.add_preferred_co_op_type(PreferredCoOpEnum.MULTIPLAYER)
    subjective_attributes_builder.add_recommend_the_ost(True)

    scraping_api = ScrapingAPI()
    wikipedia_entry = scraping_api.scrape_wikipedia_video_game_entry("The_Legend_of_Zelda:_Breath_of_the_Wild")
    metacritic_entry = scraping_api.scrape_metacritic_entry(MetacriticConsoleEnum.SWITCH, "the-legend-of-zelda-breath-of-the-wild")

    json_builder = JSONBuilder()
    json_builder.add_play_data(subjective_attributes_builder.get_play_attributes())
    json_builder.add_subjective_scoring_data(subjective_attributes_builder.get_subjective_scoring_attributes())   
    json_builder.add_wikipedia_data(wikipedia_entry)
    json_builder.add_metacritic_data(metacritic_entry)
    current_vg_name = "the_legend_of_zelda_breath_of_the_wild"
    json_builder.write_json(os.path.join(REVIEWS_DIRECTORY, f"{current_vg_name}.json"))
    online_image_saver = OnlineImageSaver(COVER_ART_DIRECTORY)
    online_image_saver.save_image(wikipedia_entry.image_url, current_vg_name)


if __name__ == "__main__":
    __main__()