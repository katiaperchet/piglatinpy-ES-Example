from src.error import PigLatinError


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
        if last_char == "y":
            return self._phrase + "nay"
        if last_char in "aeiou":
            return self._phrase + "yay"
        else:
            return self._phrase + "ay"
