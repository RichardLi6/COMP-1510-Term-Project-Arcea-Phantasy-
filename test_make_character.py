"""
Richard Maceda
A01378156
"""
from unittest import TestCase
from character import make_character


class TestMakeCharacter(TestCase):
    def test_make_character_warrior(self):
        expected_output = {
            "Class": "Warrior",
            "Health": [50, 50],
            "Attack": 9,
            "Mana": [60, 60],
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Experience": 0,
            "Inventory": [],
            "Weapon": {},
            "Armor": {},
            "Level": 1,
            "Dodge": 10,
            "Goal": [],
            "Final Boss": False,
            "Skill": {
                1: ("Double Slash", 10, 10)}
        }
        actual_character = make_character('Warrior')
        self.assertEqual(expected_output, actual_character)

    def test_make_character_ranger(self):
        expected_output = {
            "Class": "Ranger",
            "Health": [50, 50],
            "Attack": 9,
            "Mana": [60, 60],
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Experience": 0,
            "Inventory": [],
            "Weapon": {},
            "Armor": {},
            "Level": 1,
            "Dodge": 10,
            "Goal": [],
            "Final Boss": False,
            "Skill": {
                1: ("Arrow Shot", 10, 10)}
        }
        actual_character = make_character('Ranger')
        self.assertEqual(expected_output, actual_character)

    def test_make_character_mage(self):
        expected_output = {
            "Class": "Mage",
            "Health": [40, 40],
            "Attack": 9,
            "Mana": [80, 80],
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Experience": 0,
            "Inventory": [],
            "Weapon": {},
            "Armor": {},
            "Level": 1,
            "Dodge": 10,
            "Goal": [],
            "Final Boss": False,
            "Skill": {
                1: ("Fireball", 15, 10)
            }
        }
        actual_character = make_character('Mage')
        self.assertEqual(expected_output, actual_character)