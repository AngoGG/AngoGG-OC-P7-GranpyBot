#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-12-06
@note    0.0.1 (2020-12-06) : Init file
"""

from typing import Dict
from api.google_maps_api import GoogleMapsApi
from api.wiki_api import WikipediaApi
from parsing.sentence_parser import SentenceParser


class GrandPy:
    """This class is intended to drive the general application work by getting 
    the user research and returning him the bot response with APIs informations.
    """

    def __init__(self) -> None:
        """App init method.
        """
        self.google_maps: GoogleMapsApi = GoogleMapsApi()
        self.wikipedia: WikipediaApi = WikipediaApi()
        self.parser: SentenceParser = SentenceParser()

    def ask_grandpy(self, query: str) -> Dict[str, any]:
        """From a user query, return a http Response containing the localisation, the wikipedia summary and links that 
        
        Args:
            name (type): Description. Default to False.
        
        Raises:
        Returns:
        """
        sentence: str = self.parser.get_clean_sentence(query)

        location: Dict[str, float] = self.google_maps.query_by_geocode(sentence)
        wiki = self.wikipedia.query_by_geosearch(location)
        wiki_infos = self.wikipedia.get_infos_from_wikipedia(wiki[0])

        return {
            "location": location,
            "title": wiki_infos["title"],
            "summary": wiki_infos["summary"],
            "url": wiki_infos["url"],
        }
