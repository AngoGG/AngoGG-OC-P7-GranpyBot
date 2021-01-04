#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-11-30
@note    0.0.1 (2020-11-30) : Init file
"""

import os
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

    def _search_query_page(self, title: str) -> Dict[str, Any]:
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
