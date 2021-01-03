#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-11-30
@note    0.0.1 (2020-11-30) : Init file
"""

from typing import Dict


class GoogleMapsApi:
    """Google Maps API interaction class.
    """

    def __init__(self) -> None:
        """The GoogleMapsApi Constructor
        """
        ...

    def query_by_geocode(self, query: str) -> Dict[str, float]:
        """From a query return a dictionary containing latitude and longitude.

        Args:
            query (str): A string containing the query.
        Returns:
            Dict[str, float]: The location of the searched place.
        """
        ...

    def _get_coords(self, query: str) -> Dict[str, float]:
        """Query the Google Geocode API and returns the coords of the requested address.
        
        Args:
            query (str): The address requested by the user.

        Returns:
            Dict[str, float]: The location of the requested place.
        """
        ...
