#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-11-30
@note    0.0.1 (2020-11-30) : Init file
"""

import os
from typing import Any, Dict, List
import googlemaps


class GoogleMapsApi:
    """Google Maps API interaction class.
    """

    def __init__(self) -> None:
        """The GoogleMapsApi Constructor
        """

        self.gmaps: googlemaps.Client = googlemaps.Client(
            key=os.environ.get("GOOGLE_API_KEY")
        )

    def query_by_geocode(self, query: str) -> Dict[str, float]:  # pylint: disable=R1710
        """From a query return a dictionary containing latitude and longitude.

        Args:
            query (str): A string containing the query.
        Returns:
            Dict[str, float]: The location of the searched place.
        """

        maps_response: List[Dict[str, Any]] = self.gmaps.geocode(query)
        location: Dict[str, float] = maps_response[0]["geometry"]["location"]
        return location
