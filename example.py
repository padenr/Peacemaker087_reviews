import requests
from bs4 import BeautifulSoup

URL = "https://www.metacritic.com/game/pc/the-elder-scrolls-v-skyrim"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers, allow_redirects=True)
html_parser = BeautifulSoup(response.content, "html.parser")
element = html_parser.find('a', {'title': 'Video game publisher'})
print(element.text)