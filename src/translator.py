from src.error import PigLatinError

VOWEL = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxz"


class PigLatinTranslator:
    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self._phrase = phrase

    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self._phrase

    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """
        if self._phrase == "":
            return "nil"
        last_char = self._phrase[-1]
        return self._translate_word_starting_vowel(last_char)

    def _translate_word_starting_vowel(self, last_char: str) -> str:
        if last_char == "y":
            return self._phrase + "nay"
        if last_char in VOWEL:
            return self._phrase + "yay"
        if last_char in CONSONANTS:
            return self._phrase + "ay"
        else:
            raise PigLatinError
