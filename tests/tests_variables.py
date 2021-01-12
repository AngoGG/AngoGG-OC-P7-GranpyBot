from typing import Dict

geocode_data: Dict = {
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


wiki_title_search_data: Dict = {
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

wiki_geosearch_data: Dict = {
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

wiki_summary_data: Dict = {
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

wiki_url_data: Dict = {
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
