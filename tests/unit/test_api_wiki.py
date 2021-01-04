#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-11-30
@note    0.0.1 (2020-11-30) : Init file
"""

from typing import Any, Dict, List
import pytest
import requests
import mediawiki
from _pytest.monkeypatch import MonkeyPatch
from api.wiki_api import WikipediaApi

WIKI_SEARCH_DATA: Dict = {
    "batchcomplete": "",
    "continue": {"sroffset": 10, "continue": "-||"},
    "query": {
        "searchinfo": {
            "totalhits": 411694,
            "suggestion": "marie",
            "suggestionsnippet": "marie",
        },
        "search": [
            {
                "ns": 0,
                "title": "Paris",
                "pageid": 681159,
                "size": 407409,
                "wordcount": 44698,
                "snippet": 'significations, voir <span class="searchmatch">Paris</span> (homonymie). « Ville Lumière » redirige ici. Ne pas confondre avec Ville de lumière ni la villa Lumière. <span class="searchmatch">Paris</span> ([pa.ʁi]Écouter)',
                "timestamp": "2021-01-02T15:42:41Z",
            },
        ],
    },
}


class TestWikipediaApi:
    """WikipediaApi test class.
    """

    @pytest.mark.parametrize(
        "query,expected_result", [("Paris", {"page_id": 681159, "title": "Paris"}),],
    )
    def test__search_page(
        self, query: str, expected_result: Dict[str, float], monkeypatch: MonkeyPatch
    ) -> None:
        class MockRequest:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def json(self) -> Dict:
                return WIKI_SEARCH_DATA

        monkeypatch.setattr(requests, "get", MockRequest)

        wikipedia: WikipediaApi = WikipediaApi()
        wiki_response = wikipedia._search_query_page(query)

        assert wiki_response == expected_result
