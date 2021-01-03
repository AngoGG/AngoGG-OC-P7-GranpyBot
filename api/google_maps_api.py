#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-11-30
@note    0.0.1 (2020-11-30) : Init file
"""

import os
import requests
from typing import Dict


class GoogleMapsApi:
    """Google Maps API interaction class.
    """

    def __init__(self) -> None:
        """The GoogleMapsApi Constructor
        """
        self.google_maps_api_url: str = "http://maps.googleapis.com/maps/api/geocode/json"
        self.payloads: Dict = {
            "key": os.environ.get("GOOGLE_API_KEY"),
            "region": "fr",
            "address": "",
        }

    def search(self, query: str) -> Dict[str, float]:
        """From a query return a dictionary containing latitude and longitude.

        Args:
            query (str): A string containing the query.
        Returns:
            Dict[str, float]: The location of the searched place.
        """
        data = self._request(query)
        coords = data["results"][0]["geometry"]["location"]
        return coords

    def _request(self, query: str) -> Dict[str, float]:
        """Query the Google Geocode API and returns the coords of the requested address.
        
        Args:
            query (str): The address requested by the user.

        Returns:
            Dict[str, float]: The location of the requested place.
        """
        self.payloads["address"] = query
        req = requests.get(self.google_maps_api_url, params=self.payloads)
        return req.json()
