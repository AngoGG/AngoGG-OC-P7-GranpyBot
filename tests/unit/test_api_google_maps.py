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
from _pytest.monkeypatch import MonkeyPatch
from api.google_maps_api import GoogleMapsApi
from tests import tests_variables


class TestGoogleMapsApi:
    """GoogleMapsApi test class.
    """

    @pytest.fixture
    def mock_request(self, monkeypatch: MonkeyPatch):
        def _request_patch(self, query: str) -> Dict[str, float]:
            return tests_variables.geocode_data

        monkeypatch.setattr(GoogleMapsApi, "_request", _request_patch)

    @pytest.mark.parametrize(
        "query,expected_result", [("Chambly France", tests_variables.geocode_data),],
    )
    def test__request(
        self, query: str, expected_result: Dict[str, float], monkeypatch: MonkeyPatch
    ) -> None:
        class MockRequest:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def json(self) -> Dict:
                return tests_variables.geocode_data

        monkeypatch.setattr(requests, "get", MockRequest)
        google_maps: GoogleMapsApi = GoogleMapsApi()
        maps_response = google_maps._request(query)

        assert maps_response == expected_result

    @pytest.mark.parametrize(
        "query,expected_result",
        [
            (
                "Chambly France",
                {
                    "title": "60230 Chambly, France",
                    "coords": {"lat": 49.165882, "lng": 2.244301},
                },
            ),
        ],
    )
    def test_search(
        self, query: str, expected_result: Dict[str, float], mock_request
    ) -> None:

        google_maps: GoogleMapsApi = GoogleMapsApi()
        maps_response = google_maps.search("query")

        assert maps_response == expected_result

