from unittest import TestCase
from src.translator import PigLatinTranslator
from src.error import PigLatinError


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

    def test_translate_word_start_ends_vowel(self):
        # Arrange
        translator = PigLatinTranslator("epoque")
        # Act
        translation = translator.translate()
        # Assert
        self.assertEqual("epoqueyay", translation)

    def test_translate_word_start_vowel_ends_consonant(self):
        # Arrange
        translator = PigLatinTranslator("ink")
        # Act
        translation = translator.translate()
        # Assert
        self.assertEqual("inkay", translation)

    def test_translate_word_start_vowel_ends_invalid_char(self):
        # Arrange
        translator = PigLatinTranslator("ink1")
        # Act and Assert
        self.assertRaises(PigLatinError, translator.translate)

    def test_translate_word_start_consonant(self):
        # Arrange
        translator = PigLatinTranslator("hello")
        # Act
        translation = translator.translate()
        # Assert
        self.assertEqual("ellohay", translation)
