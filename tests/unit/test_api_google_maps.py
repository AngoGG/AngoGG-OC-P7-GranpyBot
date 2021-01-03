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


class TestGoogleMapsApi:
    """GoogleMapsApi test class.
    """

    @pytest.mark.parametrize(
        "query,expected_result", [("Chambly France", GEOCODE_DATA),],
    )
    def test__request(
        self, query: str, expected_result: Dict[str, float], monkeypatch: MonkeyPatch
    ) -> None:
        class MockRequest:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                return None

            def json(self) -> Dict:
                return GEOCODE_DATA

        monkeypatch.setattr(requests, "get", MockRequest)
        google_maps: GoogleMapsApi = GoogleMapsApi()
        maps_response = google_maps._request(query)

        assert maps_response == expected_result
