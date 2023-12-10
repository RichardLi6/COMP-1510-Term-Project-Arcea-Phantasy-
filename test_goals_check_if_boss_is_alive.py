"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from unittest import TestCase
from goals import check_if_boss_is_alive


class TestCheckIfBossIsAlive(TestCase):
    def test_character_killed_other_boss_except_current_boss(self):
        boss = {"Name": "North Pillar: Black Tortoise", "Health": 500, "Attack": (10, 21), "Dodge": 0,
                "Experience": 300, "ID": 1}
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Goal": [2, 3, 4]}
        actual = check_if_boss_is_alive(character, boss)
        expected = True
        self.assertEqual(expected, actual)

    def test_boss_1_is_alive(self):
        boss = {"Name": "North Pillar: Black Tortoise", "Health": 500, "Attack": (10, 21), "Dodge": 0,
                "Experience": 300, "ID": 1}
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Goal": []}
        actual = check_if_boss_is_alive(character, boss)
        expected = True
        self.assertEqual(expected, actual)

    def test_boss_1_is_dead(self):
        boss = {"Name": "North Pillar: Black Tortoise", "Health": 500, "Attack": (10, 21), "Dodge": 0,
                "Experience": 300, "ID": 1}
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Goal": [1]}
        actual = check_if_boss_is_alive(character, boss)
        expected = False
        self.assertEqual(expected, actual)

    def test_boss_2_is_alive(self):
        boss = {"Name": "East Pillar: Azure Dragon", "Health": 550, "Attack": (13, 27), "Dodge": 10,
                "Experience": 300, "ID": 2}
        character = {"X-coordinate": 1, "Y-coordinate": 23, "Goal": []}
        actual = check_if_boss_is_alive(character, boss)
        expected = True
        self.assertEqual(expected, actual)

    def test_boss_2_is_dead(self):
        boss = {"Name": "East Pillar: Azure Dragon", "Health": 550, "Attack": (13, 27), "Dodge": 10,
                "Experience": 300, "ID": 2}
        character = {"X-coordinate": 1, "Y-coordinate": 23, "Goal": [2]}
        actual = check_if_boss_is_alive(character, boss)
        expected = False
        self.assertEqual(expected, actual)

    def test_boss_3_is_alive(self):
        boss = {"Name": "West Pillar: White Tiger", "Health": 600, "Attack": (18, 38), "Dodge": 10,
                "Experience": 300, "ID": 3}
        character = {"X-coordinate": 8, "Y-coordinate": 1, "Goal": []}
        actual = check_if_boss_is_alive(character, boss)
        expected = True
        self.assertEqual(expected, actual)

    def test_boss_3_is_dead(self):
        boss = {"Name": "West Pillar: White Tiger", "Health": 600, "Attack": (18, 38), "Dodge": 10,
                "Experience": 300, "ID": 3}
        character = {"X-coordinate": 8, "Y-coordinate": 1, "Goal": [3]}
        actual = check_if_boss_is_alive(character, boss)
        expected = False
        self.assertEqual(expected, actual)

    def test_boss_4_is_alive(self):
        boss = {"Name": "South Pillar: Vermilion Bird", "Health": 700, "Attack": (20, 46), "Dodge": 20,
                "Experience": 300, "ID": 4}
        character = {"X-coordinate": 8, "Y-coordinate": 23, "Goal": []}
        actual = check_if_boss_is_alive(character, boss)
        expected = True
        self.assertEqual(expected, actual)

    def test_boss_4_is_dead(self):
        boss = {"Name": "North Pillar: Black Tortoise", "Health": 500, "Attack": (10, 21), "Dodge": 0,
                "Experience": 300, "ID": 1}
        character = {"X-coordinate": 8, "Y-coordinate": 23, "Goal": [4]}
        actual = check_if_boss_is_alive(character, boss)
        expected = False
        self.assertEqual(expected, actual)
