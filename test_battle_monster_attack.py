"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from unittest import TestCase
from battle import monster_attack
from unittest.mock import patch


class TestMonsterAttack(TestCase):
    @patch('battle.randint', return_value=1)
    def test_monster_attack_critical_hit(self, _):
        monster_1 = {"Name": "Undead", "Health": 80, "Attack": (5, 7), "Experience": 15}
        actual_character = {"Health": [50, 50]}
        monster_attack(actual_character, monster_1)
        expected_character = {"Health": [43, 50]}
        self.assertEqual(actual_character, expected_character)

    @patch('battle.randint', return_value=2)
    def test_monster_attack_non_critical_hit(self, _):
        monster_2 = {"Name": "Undead", "Health": 80, "Attack": (5, 7), "Experience": 15}
        actual_character = {"Health": [50, 50]}
        monster_attack(actual_character, monster_2)
        expected_character = {"Health": [43, 50]}
        self.assertEqual(actual_character, expected_character)
