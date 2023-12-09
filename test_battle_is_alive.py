"""
Richard Maceda
A01378156
"""
from unittest import TestCase
from battle import is_alive


class TestIsAlive(TestCase):
    def test_character_is_alive(self):
        character = {"Health": [10, 40]}
        actual = is_alive(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_character_is_not_alive(self):
        character = {"Health": [0, 40]}
        actual = is_alive(character)
        expected = False
        self.assertEqual(expected, actual)
