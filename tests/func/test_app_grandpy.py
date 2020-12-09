#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-12-08
@note    0.0.1 (2020-12-08) : Init file
"""

import pytest
from typing import Any, Dict, List
from app.grandpy import GrandPy
import mediawiki
from _pytest.monkeypatch import MonkeyPatch
from api.wiki_api import WikipediaApi
from api.google_maps_api import GoogleMapsApi


class TestGrandPy:
    @pytest.mark.parametrize(
        "query, wiki_geosearch_response, expected_result",
        [
            (
                "Chambly",
                ["Chambly (Oise)",],
                {
                    "location": {"lat": 49.165882, "lng": 2.244301},
                    "title": "Chapelle Saint-Aubin de Chambly",
                    "summary": "La Chapelle Saint-Aubin est située à Chambly.",
                    "url": "https://fr.wikipedia.org/wiki/Chapelle_Saint-Aubin_de_Chambly",
                },
            )
        ],
    )
    def test_ask_grandpy(
        self,
        query: str,
        wiki_geosearch_response: List[str],
        expected_result: Dict[str, any],
        monkeypatch: MonkeyPatch,
    ) -> None:
        class MockGoogleMapsApi:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def geocode(self, query: str) -> List[Dict[str, Any]]:
                return [{"geometry": {"location": expected_result["location"]}}]

        monkeypatch.setattr("googlemaps.Client", MockGoogleMapsApi)

        class MockMediaWiki:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def geosearch(
                self, latitude: str, longitude: str, results: int
            ) -> List[str]:
                return wiki_geosearch_response

            def page(self, query: str) -> None:
                return mediawiki.MediaWikiPage()

        class MockMediaWikiPage:
            @property
            def summary(self) -> mediawiki.MediaWikiPage:
                return expected_result["summary"]

            @property
            def url(self) -> mediawiki.MediaWikiPage:
                return expected_result["url"]

            @property
            def title(self) -> mediawiki.MediaWikiPage:
                return expected_result["title"]

        monkeypatch.setattr("mediawiki.MediaWiki", MockMediaWiki)
        monkeypatch.setattr("mediawiki.MediaWikiPage", MockMediaWikiPage)

        self.grandpy: GrandPy = GrandPy()

        assert self.grandpy.ask_grandpy(query) == expected_result
