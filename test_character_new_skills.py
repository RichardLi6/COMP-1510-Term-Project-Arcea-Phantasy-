"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from unittest import TestCase
from character import new_skills


class TestNewSkills(TestCase):
    def test_new_skill_warrior(self):
        actual_character = {
            "Level": 2, "Class": "Warrior", "Skill": {1: ("Double Slash", 10, 10)}
        }
        new_skills(actual_character, "Warrior")
        expected_character = {
            "Level": 2, "Class": "Warrior", "Skill": {1: ("Double Slash", 10, 10),
                                                      2: ("Vertical Slash", 15, 20)}
        }
        self.assertEqual(expected_character, actual_character)

    def test_new_skill_ranger(self):
        actual_character = {
            "Level": 2, "Class": "Ranger", "Skill": {1: ("Arrow Shot", 10, 10)}
        }
        new_skills(actual_character, "Ranger")
        expected_character = {
            "Level": 2, "Class": "Ranger", "Skill": {1: ("Arrow Shot", 10, 10),
                                                     2: ("Quick Slash", 15, 20)}
        }
        self.assertEqual(expected_character, actual_character)

    def test_new_skill_mage(self):
        actual_character = {
            "Level": 2, "Class": "Mage", "Skill": {1: ("Fireball", 15, 10)}
        }
        new_skills(actual_character, "Mage")
        expected_character = {
            "Level": 2, "Class": "Mage", "Skill": {1: ("Fireball", 15, 10),
                                                   2: ("Earth Fissure", 20, 20)}
        }
        self.assertEqual(expected_character, actual_character)

    def test_6th_skill_mage(self):
        actual_character = {
            "Level": 6, "Class": "Mage", "Skill": {1: ("Fireball", 15, 10),
                                                   2: ("Earth Fissure", 20, 20),
                                                   3: ("Frost Nova", 35, 45),
                                                   4: ("Chain Lightning", 50, 60),
                                                   5: ("Solar Flare", 75, 100),
                                                   }
        }
        new_skills(actual_character, "Mage")
        expected_character = {
            "Level": 6, "Class": "Mage", "Skill": {1: ("Fireball", 15, 10),
                                                   2: ("Earth Fissure", 20, 20),
                                                   3: ("Frost Nova", 35, 45),
                                                   4: ("Chain Lightning", 50, 60),
                                                   5: ("Solar Flare", 75, 100),
                                                   6: ("Ethereal Cataclysm", 100, 150)
                                                   }
        }
        self.assertEqual(expected_character, actual_character)
