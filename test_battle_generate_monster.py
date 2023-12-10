"""
Richard Maceda
A01378156
"""

from random import randint
from unittest.mock import patch
from unittest import TestCase
from battle import generate_monster


class TestGenerateMonster(TestCase):
    @patch('battle.randint', return_value=1)
    def test_generate_monster_1(self, _):
        actual_monster = generate_monster()
        expected_output = {"Name": "Slime", "Health": 60, "Attack": (7, 10), "Experience": 15}
        self.assertEqual(actual_monster, expected_output)

    @patch('battle.randint', return_value=2)
    def test_generate_monster_2(self, _):
        actual_monster = generate_monster()
        expected_output = {"Name": "Undead", "Health": 80, "Attack": (5, 7), "Experience": 15}
        self.assertEqual(actual_monster, expected_output)

    @patch('battle.randint', return_value=3)
    def test_generate_monster_3(self, _):
        actual_monster = generate_monster()
        expected_output = {"Name": "Imp", "Health": 50, "Attack": (9, 15), "Experience": 20}
        self.assertEqual(actual_monster, expected_output)

    @patch('battle.randint', return_value=4)
    def test_generate_monster_4(self, _):
        actual_monster = generate_monster()
        expected_output = {"Name": "Golem", "Health": 120, "Attack": (6, 8), "Experience": 27}
        self.assertEqual(actual_monster, expected_output)

    @patch('battle.randint', return_value=5)
    def test_generate_monster_5(self, _):
        actual_monster = generate_monster()
        expected_output = {"Name": "Fallen", "Health": 20, "Attack": (12, 15), "Experience": 10}
        self.assertEqual(actual_monster, expected_output)

    @patch('battle.randint', return_value=6)
    def test_generate_monster_6(self, _):
        actual_monster = generate_monster()
        expected_output = {"Name": "Cthulhu", "Health": 50, "Attack": (10, 10), "Experience": 15}
        self.assertEqual(actual_monster, expected_output)
