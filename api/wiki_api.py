#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-11-30
@note    0.0.1 (2020-11-30) : Init file
"""

import os
from typing import Dict, List
import mediawiki


class WikipediaApi:
    """Wikipedia API interaction class.
    """

    def __init__(self) -> None:
        """The WikipediaApi Constructor
        """

        self.wikipedia: mediawiki.MediaWiki = mediawiki.MediaWiki(lang="fr")

    def query_by_geosearch(self, position: Dict[str, float]) -> List[str]:
        """Performs a geosearch on the Wikipedia API
        Params:
            position: used to get GPS data for the search
        Returns:
            A list of results (title pages from wikipedia)"""

        return self.wikipedia.geosearch(
            latitude=position["lat"], longitude=position["lng"], results=1
        )

    def get_infos_from_wikipedia(self, query: str) -> Dict[str, str]:
        """Performs a page search on the Wikipedia API
        Params:
            query: The location we need information on.
        Returns:
            A dictionary containing the title, summary and the url link 
            from Wikipedia page for the given location.
        """

        page = self.wikipedia.page(query)

        return {"title": page.title, "summary": page.summary, "url": page.url}
