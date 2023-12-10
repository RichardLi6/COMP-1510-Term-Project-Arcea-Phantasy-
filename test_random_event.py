"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from unittest.mock import patch
from unittest import TestCase
from random_event import random_encounter


class Test(TestCase):
    @patch('random_event.randint', return_value=1)
    @patch('builtins.input', side_effect=['2'])
    def test_their_random_encounter_but_flee(self, _, __):
        character = {
            "Class": "Warrior",
            "Health": [50, 50],
            "Attack": 9,
            "Mana": [60, 60],
            "X-coordinate": 0,
            "Y-coordinate": 1,
            "Experience": 0,
            "Inventory": [],
            "Weapon": {},
            "Armor": {},
            "Level": 1,
            "Dodge": 10,
            "Goal": [],
            "Final Boss": False,
            "Skill": {
                1: ("Double Slash", 10, 10)
                }
            }
        monster = {"Name": "Slime", "Health": 60, "Attack": (7, 10), "Experience": 15}
        board = {
            (0, 0): "| |", (1, 0): "| |", (2, 0): "| |",
            (0, 1): "| |", (1, 1): "| |", (2, 1): "| |",
            (0, 2): "| |", (1, 2): "| |", (2, 2): "| |"
        }
        actual = random_encounter(monster, character, board)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random_event.randint', return_value=2)
    def test_their_random_encounter_but_fight(self, _):
        character = {
            "Class": "Warrior",
            "Health": [50, 50],
            "Attack": 9,
            "Mana": [60, 60],
            "X-coordinate": 0,
            "Y-coordinate": 1,
            "Experience": 0,
            "Inventory": [],
            "Weapon": {},
            "Armor": {},
            "Level": 1,
            "Dodge": 10,
            "Goal": [],
            "Final Boss": False,
            "Skill": {
                1: ("Double Slash", 10, 10)
                }
            }
        monster = {"Name": "Slime", "Health": 60, "Attack": (7, 10), "Experience": 15}
        board = {
            (0, 0): "| |", (1, 0): "| |", (2, 0): "| |",
            (0, 1): "| |", (1, 1): "| |", (2, 1): "| |",
            (0, 2): "| |", (1, 2): "| |", (2, 2): "| |"
        }
        actual = random_encounter(monster, character, board)
        expected = False
        self.assertEqual(expected, actual)
