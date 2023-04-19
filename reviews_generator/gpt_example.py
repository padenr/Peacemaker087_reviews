import requests

from bs4 import BeautifulSoup
from bs4.element import Tag




# Example usage: Extract the developer name of Grand Theft Auto V from its Wikipedia page
url = "https://en.wikipedia.org/wiki/Destiny_2:_Forsaken"
developer_name = find_element_after(url, 'a', {'title': 'Video game publisher'})
print("Developer name: ", developer_name)