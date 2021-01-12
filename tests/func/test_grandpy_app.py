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
from api.google_maps_api import GoogleMapsApi
from api.wiki_api import WikipediaApi


@pytest.fixture
def mock_google_maps_search(monkeypatch: MonkeyPatch):
    def search_patch(self, query: str) -> Dict[str, float]:
        return {
            "address": "60230 Chambly, France",
            "coords": {"lat": 49.165882, "lng": 2.244301},
        }

    monkeypatch.setattr(GoogleMapsApi, "search", search_patch)


@pytest.fixture
def mock_wiki_get_page_info_from_title(monkeypatch: MonkeyPatch):
    def get_page_info_patch(
        self, gmaps_title: str, gmaps_coords: Dict[str, float]
    ) -> Dict[str, Any]:
        return {
            "page_info": {
                "title": "Paris",
                "summary": "Paris ([pa.ʁi]) est la commune la plus peuplée et la capitale de la France.\n",
                "url": "https://fr.wikipedia.org/wiki/Paris",
            },
            "search_type": "title",
        }

    monkeypatch.setattr(WikipediaApi, "get_page_info", get_page_info_patch)


@pytest.fixture
def mock_wiki_get_page_info_from_coords(monkeypatch: MonkeyPatch):
    def get_page_info_patch(
        self, gmaps_title: str, gmaps_coords: Dict[str, float]
    ) -> Dict[str, Any]:
        return {
            "page_info": {
                "title": "Paris",
                "summary": "Paris ([pa.ʁi]) est la commune la plus peuplée et la capitale de la France.\n",
                "url": "https://fr.wikipedia.org/wiki/Paris",
            },
            "search_type": "coords",
        }

    monkeypatch.setattr(WikipediaApi, "get_page_info", get_page_info_patch)


class TestApp:
    @pytest.mark.parametrize(
        "query, expected_result",
        [
            (
                "Chambly",
                {
                    "info": {
                        "location": {"lat": 49.165882, "lng": 2.244301},
                        "title": "Paris",
                        "summary": "Paris ([pa.ʁi]) est la commune la plus peuplée et la capitale de la France.\n",
                        "url": "https://fr.wikipedia.org/wiki/Paris",
                    },
                    "search_type": "title",
                },
            )
        ],
    )
    def test_answer_from_title(
        self,
        query: str,
        expected_result: Dict[str, any],
        mock_google_maps_search,
        mock_wiki_get_page_info_from_title,
    ) -> None:

        self.grandpy: App = App()

        assert self.grandpy.answer(query) == expected_result

    @pytest.mark.parametrize(
        "query, expected_result",
        [
            (
                "Chambly",
                {
                    "info": {
                        "location": {"lat": 49.165882, "lng": 2.244301},
                        "address": "60230 Chambly, France",
                        "summary": "Paris ([pa.ʁi]) est la commune la plus peuplée et la capitale de la France.\n",
                        "url": "https://fr.wikipedia.org/wiki/Paris",
                    },
                    "search_type": "coords",
                },
            )
        ],
    )
    def test_answer_from_title(
        self,
        query: str,
        expected_result: Dict[str, any],
        mock_google_maps_search,
        mock_wiki_get_page_info_from_coords,
    ) -> None:

        self.grandpy: App = App()

        assert self.grandpy.answer("KO Title") == expected_result
