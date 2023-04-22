from reviews_metadata_generator.data_scraping.data_scraper import MetacriticScraper, MetacriticConsoleEnum, WikipediaVideoGameEntryScraper 
from reviews_metadata_generator.data_scraping.game_metadata_datatypes import WikipediaEntry, MetacriticEntry


class ScrapingAPI: 

    def scrape_wikipedia_video_game_entry(self, wiki_page_title: str) -> WikipediaEntry:
        scraper = WikipediaVideoGameEntryScraper(wiki_page_title)
        wikipedia_entry = WikipediaEntry()
        wikipedia_entry.title = scraper.get_wiki_entry_title()
        wikipedia_entry.developers = scraper.get_value_from_header('developers', sub_strings_to_strip='[a]')
        wikipedia_entry.directors = scraper.get_value_from_header('directors')
        wikipedia_entry.publishers = scraper.get_value_from_header('publishers')
        wikipedia_entry.composers = scraper.get_value_from_header('composers')
        wikipedia_entry.series = scraper.get_value_from_header('series')
        wikipedia_entry.platforms = scraper.get_value_from_header('platforms')
        wikipedia_entry.release_data = scraper.get_value_from_header('release')
        wikipedia_entry.genres = scraper.get_value_from_header('genres')
        wikipedia_entry.image_url = scraper.get_wiki_entry_image_url()
        return wikipedia_entry
    
    def scrape_metacritic_entry(self, console_enum: MetacriticConsoleEnum, game_title: str) -> MetacriticEntry:
        scraper = MetacriticScraper(console_enum, game_title)
        metacritic_entry = MetacriticEntry()
        metacritic_entry.metascore = scraper.get_metascore()
        metacritic_entry.user_score = scraper.get_user_score()
        metacritic_entry.rating = scraper.get_rating()
        return metacritic_entry
