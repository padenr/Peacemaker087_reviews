## What is needed for video game reviews ##

class VideoGameReviewsMetadataBuilder:

    def __init__(self, video_game_name):
        pass

    """
        The group or anthology the game is a part of
    """

    def add_series(self, series_name):
        pass

    """
        Total Score (1.x-10) x=0-9
    """

    def add_total_score(self, score: float) -> None:
        pass

    """ 
        Narrative Ratings
            - N/A
            - Lore (1-5 stars)
            - Traditional Narrative (1-5 stars)
    """

    def add_narrative_rating(self, narrative_type: str, stars=None: int) -> None: 
        pass 

    """ 
        Gameplay Ratings
            - 
    """ 

    def add_gameplay_rating(self):
        pass

    """
        Graphics Ratings
            - Timeless
            - Artistically-Subjective 
                - good
                - bad 
            - For the Reviewed Time Period (1-5 stars)
            - When the game came out (1-5 stars) 
    """

    def add_graphics_rating(self, graphics_type: str, artistic_rating=None: str, stars=None: int) -> None:
        pass

    """
        The game is better played with friends if true.
        Preferred co-op type:
            - Online Multiplayer
            - Splitscreen
            - Controller Pass
            - Party Game
    """
    
    def add_better_with_friends(self, is_better: bool, preferred_co_op_type) -> None:
        pass


# Better with friends? 
# Estimated Length to Average Completion
# Hours Played
# Completed? 
# Recommend the OST? 

# Timeless? 

# Spoilers? 

#Metacritic - Critic
#Metacritic - Audience
#IGN
#Polygon
#GameSpot
#PC Gamer

#Genre

#Release Date
#Most Recent Played Date

