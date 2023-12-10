"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from unittest import TestCase
from battle import after_fight


class TestAfterFight(TestCase):
    def test_after_fight(self):
        monster = {"Name": "Cthulhu", "Health": 50, "Attack": (10, 10), "Experience": 15}
        actual_character = {"Health": [10, 50], "Mana": [10, 80], "Experience": 0}
        after_fight(actual_character, monster)
        expected_character = {"Health": [35, 50], "Mana": [45, 80], "Experience": 15}
        self.assertEqual(expected_character, actual_character)
