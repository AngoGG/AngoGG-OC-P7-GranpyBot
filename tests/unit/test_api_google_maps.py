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
from api.google_maps_api import GoogleMapsApi


class TestGoogleMapsApi:
    """GoogleMapsApi test class.
    """

    @pytest.mark.parametrize(
        "query,expected_result",
        [
            ("Chambly France", {"lat": 49.165882, "lng": 2.244301}),
            ("Paris", {"lat": 48.856614, "lng": 2.3522219}),
        ],
    )
    def test_geocode(
        self, query: str, expected_result: Dict[str, float], monkeypatch: MonkeyPatch
    ) -> None:
        """The query_by_geocode test method.
        Check if the method returns a right Dictionnary from a query.
        """

        class MockResponse:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def geocode(self, query: str) -> List[Dict[str, Any]]:
                return [{"geometry": {"location": expected_result}}]

        monkeypatch.setattr("googlemaps.Client", MockResponse)

        google_maps: GoogleMapsApi = GoogleMapsApi()
        maps_response = google_maps.query_by_geocode(query)

        assert maps_response == expected_result

