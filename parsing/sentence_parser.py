#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-12-01
@note    0.0.1 (2020-12-01) : Init file
"""
from typing import List
import pytest
import re


class SentenceParser:
    """Class which handle the user query parsing to query the APIs.
    """

    def split_words(self, sentence: str) -> List[str]:
        """This method splits a sentence string to a list of words.
        
        Args:
            sentence (str): A user sentence.
        
        Returns:
            A list of all user sentence words.
        """

        splitted_words: List[str] = re.split(r"\W", sentence)

        return list(filter(None, splitted_words))
