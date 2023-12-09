"""
Richard Maceda
A01378156
"""
from unittest import TestCase
from battle import heal_character


class TestHealCharacter(TestCase):
    def test_heal_character_at_level_1(self):
        actual_character = {"Health": [11, 50], "Mana": [20, 60], "Level": 1}
        heal_character(actual_character)
        expected_character = {"Health": [22, 50], "Mana": [33, 60], "Level": 1}
        self.assertEqual(expected_character, actual_character)

    def test_heal_character_at_level_3(self):
        actual_character = {"Health": [11, 125], "Mana": [20, 120], "Level": 3}
        heal_character(actual_character)
        expected_character = {"Health": [28, 125], "Mana": [41, 120], "Level": 3}
        self.assertEqual(expected_character, actual_character)

    def test_heal_character_at_level_6(self):
        actual_character = {"Health": [11, 150], "Mana": [20, 180], "Level": 6}
        heal_character(actual_character)
        expected_character = {"Health": [39, 150], "Mana": [55, 180], "Level": 6}
        self.assertEqual(expected_character, actual_character)
