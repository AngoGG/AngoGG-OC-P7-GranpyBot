#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-11-30
@note    0.0.1 (2020-11-30) : Init file
"""

import os
import random
import requests
import urllib.parse
from typing import Any, Dict, List


class WikipediaApi:
    """Wikipedia API interaction class.
    """

    def __init__(self) -> None:
        """The WikipediaApi Constructor
        """
        self.wiki_api_url: str = "https://fr.wikipedia.org/w/api.php"

    def _search_page_by_title(self, title: str) -> Dict[str, Any]:
        """Search for similar titles on Wiki API
        
        Args:
            title (str): Page title.
        
        Returns:
            Dict[str, Any]: Page ID and title of the API response page.
        """
        params: Dict = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": title,
        }
        req = requests.get(self.wiki_api_url, params=params)

        data = req.json()
        return {
            "page_id": data["query"]["search"][0]["pageid"],
            "title": data["query"]["search"][0]["title"],
        }

    def _search_page_by_geo(self, coords: Dict[str, float]) -> Dict[str, Any]:
        """Search and returns a random page near the given coords.  
        
        Args:
            coords (str): Location Coords.
        
        Returns:
            Dict[str, Any]: Page ID and title of the API response page.
        """
        lat = str(coords["lat"])
        lng = str(coords["lng"])
        params: Dict = {
            "action": "query",
            "format": "json",
            "list": "geosearch",
            "gscoord": f"{lat}|{lng}",
        }
        req = requests.get(self.wiki_api_url, params=params)

        data = random.choice(req.json()["query"]["geosearch"])
        return {
            "page_id": data["pageid"],
            "title": data["title"],
        }

    def _get_page_summary(self, page_id: int) -> Dict[str, Any]:
        """Method Description.
        Description details here (if needed).
        
        Args:
            name (type): Description. Default to False.
        
        Raises:
        Returns:
        """
        params: Dict = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "pageids": page_id,
            "formatversion": "latest",
            "exsentences": 3,
            "explaintext": True,
        }

        req = requests.get(self.wiki_api_url, params=params)

        return req.json()["query"]["pages"][0]["extract"]

    def _get_page_url(self, page_id: int) -> Dict[str, Any]:
        """Method Description.
        Description details here (if needed).
        
        Args:
            name (type): Description. Default to False.
        
        Raises:
        Returns:
        """
        params: Dict = {
            "action": "query",
            "format": "json",
            "prop": "info",
            "inprop": "url",
            "pageids": page_id,
        }

        req = requests.get(self.wiki_api_url, params=params)

        return req.json()["query"]["pages"][str(page_id)]["fullurl"]
