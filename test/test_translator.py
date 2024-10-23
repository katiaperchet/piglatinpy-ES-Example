from unittest import TestCase
from src.translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        # Arrange
        translator = PigLatinTranslator("hello world")
        # Act
        phrase = translator.get_phrase()
        # Assert
        self.assertEqual("hello world", phrase)

    def test_translate_empty_string(self):
        # Arrange
        translator = PigLatinTranslator("")
        # Act
        translation = translator.translate()
        # Assert
        self.assertEqual("nil", translation)

    def test_translate_word_start_vowel_ending_y(self):
        # Arrange
        translator = PigLatinTranslator("any")
        # Act
        translation = translator.translate()
        # Assert
        self.assertEqual("anynay", translation)

