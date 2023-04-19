def get_metacritic_URL(metacritic_console: str, metacritic_game_title: str) -> str:
    ROOT_URL = "https://www.metacritic.com/game/"
    return f"{ROOT_URL}{metacritic_console}/{metacritic_game_title}"

def get_wikipedia_URL(wiki_page_title: str) -> str:
    ROOT_URL = "https://en.wikipedia.org/wiki/"
    return f"{ROOT_URL}/{wiki_page_title}"