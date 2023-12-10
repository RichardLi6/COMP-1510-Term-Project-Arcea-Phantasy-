"""
Richard Maceda
A01378156
"""
from unittest import TestCase
from battle import passive_regeneration


class TestPassiveRegeneration(TestCase):
    def test_passive_regeneration(self):
        actual_character = {"Health": [10, 50], "Mana": [10, 80]}
        passive_regeneration(actual_character)
        expected_character = {"Health": [14, 50], "Mana": [15, 80]}
        self.assertEqual(expected_character, actual_character)