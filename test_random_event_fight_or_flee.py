"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from unittest.mock import patch
from unittest import TestCase
from random_event import fight_or_flee


class TestFightOrFlee(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_fight(self, _):
        monster = {"Name": "Fallen", "Health": 20, "Attack": (12, 15), "Experience": 10}
        actual = fight_or_flee(monster)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_flee(self, _):
        monster = {"Name": "Fallen", "Health": 20, "Attack": (12, 15), "Experience": 10}
        actual = fight_or_flee(monster)
        expected = False
        self.assertEqual(expected, actual)