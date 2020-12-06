#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-12-06
@note    0.0.1 (2020-12-06) : Init file
"""

import pytest
from parsing.sentence_parser import SentenceParser


class TestSentenceParser:
    @pytest.mark.parametrize(
        "query, expected_result",
        [
            (
                "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?",
                "salut grandpy connais adresse openclassrooms",
            )
        ],
    )
    def test_get_clean_sentence(self, query: str, expected_result: str) -> None:
        """The get_sentence test method.
        Check if the method returns a correct sentence string from a user query.
        """

        parser: SentenceParser = SentenceParser()
        sentence = parser.get_clean_sentence(query)

        assert sentence == expected_result
