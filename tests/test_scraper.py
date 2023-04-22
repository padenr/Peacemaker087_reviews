import requests

from reviews_metadata_generator.data_scraping.data_scraper import Scraper, WikipediaVideoGameEntryScraper
from reviews_metadata_generator.data_scraping.data_scraper import MetacriticScraper, MetacriticConsoleEnum

###############################################
#                Scraper Tests                #
###############################################


class TestScraper:

    @classmethod
    def setup_class(cls):
        cls.URL = "https://en.wikipedia.org/wiki/The_Elder_Scrolls_V:_Skyrim"
        response = requests.get(cls.URL)
        cls.scraper = Scraper(response)

    def test_find_table_element_by_row_header(self):
        element = self.scraper.find_table_element_by_row_header('table', {'class': 'infobox ib-video-game hproduct'}, 'Developer(s)')
        assert element.text == "Bethesda Game Studios[a]"

    def test_find_element_with_offset(self):
        element = self.scraper.find_element_with_offset('table', {'class': 'infobox ib-video-game hproduct'}, offset=3)
        assert element.text == "The Elder Scrolls V: Skyrim"


###############################################
#            Wikipedia Scraper Tests          #
###############################################


class TestWikipediaVideoGameEntryScraper:

    @classmethod
    def setup_class(cls):
        cls.scraper = WikipediaVideoGameEntryScraper("The_Elder_Scrolls_V:_Skyrim")

    def test_get_wiki_entry_image_url(self):
        actual_image_url = self.scraper.get_wiki_entry_image_url()
        expected_image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/1/15/The_Elder_Scrolls_V_Skyrim_cover.png/220px-The_Elder_Scrolls_V_Skyrim_cover.png"
        assert actual_image_url == expected_image_url

    def test_get_value_from_header(self):
        actual_developers = self.scraper.get_value_from_header('developers', '[a]')
        expected_developers = ["Bethesda Game Studios"]
        assert actual_developers == expected_developers


###############################################
#            Metacritic Scraper Tests         #
###############################################


class TestMetacriticScraper:

    @classmethod
    def setup_class(cls):
        cls.scraper = MetacriticScraper(MetacriticConsoleEnum.PS4, "red-dead-redemption-2")

    def test_get_metascore(self):
        actual_metascore = self.scraper.get_metascore()
        expected_metascore = 97
        assert actual_metascore == expected_metascore

    def test_get_user_score(self):
        actual_user_score = self.scraper.get_user_score()
        expected_user_score = 8.7
        assert actual_user_score == expected_user_score

    def test_get_rating(self):
        actual_rating = self.scraper.get_rating()
        expected_rating = 'M'
        assert actual_rating == expected_rating