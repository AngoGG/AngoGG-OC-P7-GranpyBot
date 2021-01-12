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
import api.wiki_api
from tests import tests_variables


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
                return tests_variables.wiki_title_search_data

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
                return tests_variables.wiki_geosearch_data

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
                return tests_variables.wiki_summary_data

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
                return tests_variables.wiki_url_data

        monkeypatch.setattr(requests, "get", MockRequest)

        wikipedia: WikipediaApi = WikipediaApi()
        wiki_response = wikipedia._get_page_url(query)

        assert wiki_response == expected_result

    @pytest.fixture
    def mock__search_page_by_title(self, monkeypatch: MonkeyPatch):
        def _search_page_by_title_patch(self, title: str) -> Dict[str, Any]:
            return {"page_id": 681159, "title": "Paris"}

        monkeypatch.setattr(
            WikipediaApi, "_search_page_by_title", _search_page_by_title_patch
        )

    @pytest.fixture
    def mock__search_page_by_geo(self, monkeypatch: MonkeyPatch) -> str:
        def _search_page_by_geo_patch(self, page_id: int) -> str:
            return {"page_id": 681159, "title": "Title from coords"}

        monkeypatch.setattr(
            WikipediaApi, "_search_page_by_geo", _search_page_by_geo_patch
        )

    @pytest.fixture
    def mock__get_page_summary(self, monkeypatch: MonkeyPatch) -> str:
        def _get_page_summary_patch(self, page_id: int) -> str:
            return "Paris ([pa.ʁi]) est la commune la plus peuplée et la capitale de la France.\n"

        monkeypatch.setattr(WikipediaApi, "_get_page_summary", _get_page_summary_patch)

    @pytest.fixture
    def mock__get_page_url(self, monkeypatch: MonkeyPatch) -> str:
        def _get_page_url_patch(self, page_id: int) -> str:
            return "https://fr.wikipedia.org/wiki/Paris"

        monkeypatch.setattr(WikipediaApi, "_get_page_url", _get_page_url_patch)

    @pytest.mark.skip(reason="Title search is no longer used")
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
        self,
        query: str,
        expected_result: Dict[str, float],
        monkeypatch: MonkeyPatch,
        mock__search_page_by_title,
        mock__get_page_summary,
        mock__get_page_url,
    ) -> None:

        wikipedia: WikipediaApi = WikipediaApi()
        wiki_response = wikipedia.get_page_info(query["title"], query["coords"])

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
                        "title": "Title from coords",
                        "summary": "Paris ([pa.ʁi]) est la commune la plus peuplée et la capitale de la France.\n",
                        "url": "https://fr.wikipedia.org/wiki/Paris",
                    },
                    "search_type": "coords",
                },
            ),
        ],
    )
    def test__get_page_info(
        self,
        query: str,
        expected_result: Dict[str, float],
        monkeypatch: MonkeyPatch,
        mock__search_page_by_title,
        mock__search_page_by_geo,
        mock__get_page_summary,
        mock__get_page_url,
    ) -> None:

        wikipedia: WikipediaApi = WikipediaApi()
        wiki_response = wikipedia.get_page_info("Fake title", query["coords"])

        assert wiki_response == expected_result
