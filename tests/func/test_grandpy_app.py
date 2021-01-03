#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-12-08
@note    0.0.1 (2020-12-08) : Init file
"""

import pytest
import requests
from typing import Any, Dict, List
from grandpy.app import App
import mediawiki
from _pytest.monkeypatch import MonkeyPatch
from api.wiki_api import WikipediaApi

GEOCODE_DATA: Dict = {
    "results": [
        {
            "address_components": [
                {
                    "long_name": "Chambly",
                    "short_name": "Chambly",
                    "types": ["locality", "political"],
                },
                {
                    "long_name": "Oise",
                    "short_name": "Oise",
                    "types": ["administrative_area_level_2", "political"],
                },
                {
                    "long_name": "Hauts-de-France",
                    "short_name": "Hauts-de-France",
                    "types": ["administrative_area_level_1", "political"],
                },
                {
                    "long_name": "France",
                    "short_name": "FR",
                    "types": ["country", "political"],
                },
                {"long_name": "60230", "short_name": "60230", "types": ["postal_code"]},
            ],
            "formatted_address": "60230 Chambly, France",
            "geometry": {
                "bounds": {
                    "northeast": {"lat": 49.1972119, "lng": 2.275515},
                    "southwest": {"lat": 49.1513141, "lng": 2.216646},
                },
                "location": {"lat": 49.165882, "lng": 2.244301},
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {"lat": 49.1972119, "lng": 2.275515},
                    "southwest": {"lat": 49.1513141, "lng": 2.216646},
                },
            },
            "place_id": "ChIJ3Y877GNa5kcR6Qy4YnzvNPw",
            "types": ["locality", "political"],
        }
    ],
    "status": "OK",
}


class TestApp:
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
    def test_answer(
        self,
        query: str,
        wiki_geosearch_response: List[str],
        expected_result: Dict[str, any],
        monkeypatch: MonkeyPatch,
    ) -> None:
        class MockRequest:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def json(self) -> Dict:
                return GEOCODE_DATA

        monkeypatch.setattr(requests, "get", MockRequest)

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

        self.grandpy: App = App()

        assert self.grandpy.answer(query) == expected_result
