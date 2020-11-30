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
from _pytest.monkeypatch import MonkeyPatch
from api.wiki_api import WikipediaApi


class TestWikipediaApi:
    """WikipediaApi test class.
    """

    @pytest.mark.parametrize(
        "query,expected_result",
        [
            ({"lat": 49.165882, "lng": 2.244301}, ["Chambly (Oise)",],),
            ({"lat": 48.856614, "lng": 2.3522219}, ["Jeux olympiques d'été de 2024"],),
        ],
    )
    def test_query_by_geosearch(
        self,
        query: Dict[str, float],
        expected_result: List[str],
        monkeypatch: MonkeyPatch,
    ) -> None:
        """The query_by_geosearch test method.
        Check if the method returns a right List from a query.
        """

        class MockResponse:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def geosearch(
                self, latitude: str, longitude: str, results: int
            ) -> List[str]:
                return expected_result

        monkeypatch.setattr("mediawiki.MediaWiki", MockResponse)

        wikipedia: WikipediaApi = WikipediaApi()
        wiki_response = wikipedia.query_by_geosearch(query)

        assert wiki_response == expected_result
