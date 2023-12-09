"""
Richard Maceda
A1378156
"""
from unittest import TestCase
from character import level_up


class TestLevelUp(TestCase):
    def test_level_up_warrior(self):
        actual_character = {
            "Class": "Warrior",
            "Health": [50, 50],
            "Attack": 9,
            "Mana": [60, 60],
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Experience": 41,
            "Level": 1,
            "Final Boss": False,
            "Skill": {
                1: ("Double Slash", 10, 10)
            }
        }
        level_up(actual_character, 'Warrior')

        expected_character = {
            "Class": "Warrior",
            "Health": [50, 75],
            "Attack": 16,
            "Mana": [60, 80],
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Experience": 1,
            "Level": 2,
            "Final Boss": False,
            "Skill": {
                1: ("Double Slash", 10, 10), 2: ('Vertical Slash', 15, 20)}
        }

        self.assertEqual(expected_character, actual_character)

    def test_level_up_warrior_4(self):
        actual_character = {
            "Class": "Warrior",
            "Health": [100, 100],
            "Attack": 30,
            "Mana": [60, 60],
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Experience": 131,
            "Level": 3,
            "Final Boss": False,
            "Skill": {
                1: ("Double Slash", 10, 10), 2: ('Vertical Slash', 15, 20), 3: ("Riptide Slash", 25, 30)
            }
        }
        level_up(actual_character, 'Warrior')

        expected_character = {
            "Class": "Warrior",
            "Health": [100, 125],
            "Attack": 37,
            "Mana": [60, 80],
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Experience": 41,
            "Level": 4,
            "Final Boss": False,
            "Skill": {
                1: ("Double Slash", 10, 10), 2: ('Vertical Slash', 15, 20), 3: ("Riptide Slash", 25, 30),
                4: ("Brutal Cleave", 45, 50)
            }
        }

        self.assertEqual(expected_character, actual_character)

