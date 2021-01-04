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


WIKI_TITLE_SEARCH_DATA: Dict = {
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
                "snippet": 'significations, voir <span class="searchmatch">Paris</span> (homonymie)',
                "timestamp": "2021-01-02T15:42:41Z",
            },
        ],
    },
}

WIKI_GEOSEARCH_DATA: Dict = {
    "batchcomplete": "",
    "query": {
        "geosearch": [
            {
                "pageid": 3120649,
                "ns": 0,
                "title": "Quai de la Gironde",
                "lat": 48.8965,
                "lon": 2.383164,
                "dist": 114.2,
                "primary": "",
            },
            {
                "pageid": 11988883,
                "ns": 0,
                "title": "Parc du Pont de Flandre",
                "lat": 48.89694,
                "lon": 2.38194,
                "dist": 124.4,
                "primary": "",
            },
            {
                "pageid": 3124793,
                "ns": 0,
                "title": "Square du Quai-de-la-Gironde",
                "lat": 48.896194,
                "lon": 2.383181,
                "dist": 147.8,
                "primary": "",
            },
        ]
    },
}

WIKI_SUMMARY_DATA: Dict = {
    "batchcomplete": True,
    "query": {
        "pages": [
            {
                "pageid": 681159,
                "ns": 0,
                "title": "Paris",
                "extract": "Paris ([pa.ʁi]) est la commune la plus peuplée et la capitale de la France.\n",
            }
        ]
    },
}

WIKI_URL_DATA: Dict = {
    "batchcomplete": "",
    "query": {
        "pages": {
            "681159": {
                "pageid": 681159,
                "ns": 0,
                "title": "Paris",
                "contentmodel": "wikitext",
                "pagelanguage": "fr",
                "pagelanguagehtmlcode": "fr",
                "pagelanguagedir": "ltr",
                "touched": "2021-01-04T15:20:46Z",
                "lastrevid": 178406474,
                "length": 407435,
                "fullurl": "https://fr.wikipedia.org/wiki/Paris",
                "editurl": "https://fr.wikipedia.org/w/index.php?title=Paris&action=edit",
                "canonicalurl": "https://fr.wikipedia.org/wiki/Paris",
            }
        }
    },
}


class TestWikipediaApi:
    """WikipediaApi test class.
    """

    @pytest.mark.parametrize(
        "query,expected_result", [("Paris", {"page_id": 681159, "title": "Paris"}),],
    )
    def test__search_page_by_title(
        self, query: str, expected_result: Dict[str, float], monkeypatch: MonkeyPatch
    ) -> None:
        class MockRequest:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def json(self) -> Dict:
                return WIKI_TITLE_SEARCH_DATA

        monkeypatch.setattr(requests, "get", MockRequest)

        wikipedia: WikipediaApi = WikipediaApi()
        wiki_response = wikipedia._search_page_by_title(query)

        assert wiki_response == expected_result

    @pytest.mark.parametrize(
        "query,expected_result",
        [
            (
                {"lat": 48.856614, "lng": 2.3522219},
                [
                    {"page_id": 3120649, "title": "Quai de la Gironde"},
                    {"page_id": 11988883, "title": "Parc du Pont de Flandre"},
                    {"page_id": 3124793, "title": "Square du Quai-de-la-Gironde"},
                ],
            ),
        ],
    )
    def test__search_page_by_geo(
        self, query: str, expected_result: Dict[str, float], monkeypatch: MonkeyPatch
    ) -> None:
        class MockRequest:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def json(self) -> Dict:
                return WIKI_GEOSEARCH_DATA

        monkeypatch.setattr(requests, "get", MockRequest)

        wikipedia: WikipediaApi = WikipediaApi()
        wiki_response = wikipedia._search_page_by_geo(query)

        assert wiki_response in expected_result

    @pytest.mark.parametrize(
        "query,expected_result",
        [
            (
                681159,
                "Paris ([pa.ʁi]) est la commune la plus peuplée et la capitale de la France.\n",
            ),
        ],
    )
    def test__get_page_summary(
        self, query: str, expected_result: Dict[str, float], monkeypatch: MonkeyPatch
    ) -> None:
        class MockRequest:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def json(self) -> Dict:
                return WIKI_SUMMARY_DATA

        monkeypatch.setattr(requests, "get", MockRequest)

        wikipedia: WikipediaApi = WikipediaApi()
        wiki_response = wikipedia._get_page_summary(query)

        assert wiki_response in expected_result

    @pytest.mark.parametrize(
        "query,expected_result", [(681159, "https://fr.wikipedia.org/wiki/Paris",),],
    )
    def test__get_page_url(
        self, query: str, expected_result: Dict[str, float], monkeypatch: MonkeyPatch
    ) -> None:
        class MockRequest:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def json(self) -> Dict:
                return WIKI_URL_DATA

        monkeypatch.setattr(requests, "get", MockRequest)

        wikipedia: WikipediaApi = WikipediaApi()
        wiki_response = wikipedia._get_page_url(query)

        assert wiki_response == expected_result

    @pytest.mark.parametrize(
        "query,expected_result",
        [
            (
                {
                    "title": "Paris, France",
                    "coords": {"lat": 48.856614, "lng": 2.3522219},
                },
                {
                    "page_info": {
                        "title": "Paris",
                        "summary": "Paris ([pa.ʁi]) est la commune la plus peuplée et la capitale de la France.\n",
                        "url": "https://fr.wikipedia.org/wiki/Paris",
                    },
                    "search_type": "title",
                },
            ),
        ],
    )
    def test__get_page_info_ok_title(
        self, query: str, expected_result: Dict[str, float], monkeypatch: MonkeyPatch
    ) -> None:
        class MockWikipediaApi:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def _search_page_by_title(self, coords: Dict[str, float]) -> Dict:
                return {"page_id": 681159, "title": "Paris"}

            def _get_page_summary(self, coords: Dict[str, float]) -> Dict:
                return "Paris ([pa.ʁi]) est la commune la plus peuplée et la capitale de la France.\n"

            def _get_page_url(self, coords: Dict[str, float]) -> Dict:
                return "https://fr.wikipedia.org/wiki/Paris"

        monkeypatch.setattr("api.wiki_api.WikipediaApi", MockWikipediaApi)

        wikipedia: WikipediaApi = WikipediaApi()
        wiki_response = wikipedia.get_page_info(query["title"], query["coords"])

        assert wiki_response == expected_result
