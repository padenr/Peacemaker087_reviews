import requests

from requests import Response
from PIL import Image

from bs4 import BeautifulSoup
from bs4.element import Tag

from abc import ABC
from enum import Enum


class MetacriticConsoleEnum(Enum):

    XBOX_360 = "xbox-360"
    PS3 = "playstation-3"
    PC = "pc"
    PS4 = "playstation-4"
    SWITCH = "switch"
    

class Scraper(ABC): 

    def __init__(self, page: Response):
        self.__html_parser = BeautifulSoup(page.content, "html.parser")

    def find_element(self, tag, identifier) -> Tag:
        return self.__html_parser.find(tag, identifier)
    
    def find_table_element_by_row_header(self, tag, identifier, header_value) -> Tag:
        next_element = None
        table_element = self.find_element(tag, identifier)
        for element in table_element.find_all('th'):
            if element.text == header_value:
                next_element = element.find_next('td')
                break
        return next_element
    
    def find_element_with_offset(self, tag, identifier, offset) -> Tag:
        element = self.find_element(tag, identifier)
        for _ in range(offset):
            element = element.find_next()
        return element


class WikipediaVideoGameEntryScraper:

    ROOT_URL = "https://en.wikipedia.org/wiki/"
    ELEMENT_SIMPLIFIER_MAP = {
                                "developers": "Developer(s)",
                                "publishers": "Publisher(s)",
                                "series": "Series",
                                "platforms": "Platform(s)",
                                "composers": "Composer(s)",
                                "directors": "Director(s)",
                                "release": "Release",
                                "genres": "Genre(s)"
                             }

    def __init__(self, wiki_page_title: str):
        URL = f"{self.ROOT_URL}{wiki_page_title}"
        self.__scraper = Scraper(requests.get(URL))

    def get_wiki_entry_title(self) -> str:
        return self.__scraper.find_element('h1', {'id': 'firstHeading'}).text

    def get_wiki_entry_image_url(self):
        image_element = self.__scraper.find_element_with_offset('td', {'class': 'infobox-image'}, 2)
        if image_element == None:
            return None
        image_url = "https:" + image_element.get('src')
        return image_url

    def get_value_from_header(self, header_value: str, sub_strings_to_strip: list = []) -> list:
        header_values = []
        wikipedia_value = self.ELEMENT_SIMPLIFIER_MAP[header_value]
        header_element = self.__scraper.find_table_element_by_row_header('table', {'class': 'infobox ib-video-game hproduct'}, wikipedia_value)
        if header_element == None:
            return header_values
        for header_value in header_element.find_all(text=True):
            if header_value not in sub_strings_to_strip:
                header_values.append(header_value)
        return header_values


class MetacriticScraper():

    ROOT_URL = "https://www.metacritic.com/game/"
    #Specify the user agent to avoid redirects
    HEADERS = {"User-Agent": "Mozilla/5.0"}


    def __init__(self, metacritic_console: MetacriticConsoleEnum, metacritic_game_title: str):
        super().__init__()
        URL = f"{self.ROOT_URL}{metacritic_console.value}/{metacritic_game_title}" 
        self.__scraper = Scraper(requests.get(URL, headers=self.HEADERS, allow_redirects=False))

    def get_metascore(self) -> int:
        metascore = self.__scraper.find_element('div', {'class': 'metascore_w xlarge game positive'})
        if metascore == None:
            return None
        return int(metascore.text)

    def get_user_score(self) -> float:
        user_score = self.__scraper.find_element('div', {'class': 'metascore_w user large game positive'})
        if user_score == None:
            return None
        return float(user_score.text)
    
    def get_rating(self) -> str:
        rating = self.__scraper.find_element_with_offset('li', {'class': 'summary_detail product_rating'}, 2)
        if rating == None:
            return None
        return rating.text

        