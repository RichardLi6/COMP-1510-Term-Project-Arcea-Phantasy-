"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from unittest import TestCase
from goals import which_boss
from unittest.mock import patch


class TestWhichBoss(TestCase):
    def test_boss_1(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = which_boss(character)
        expected = 1
        self.assertEqual(expected, actual)

    def test_boss_2(self):
        character = {"X-coordinate": 1, "Y-coordinate": 23}
        actual = which_boss(character)
        expected = 2
        self.assertEqual(expected, actual)

    def test_boss_3(self):
        character = {"X-coordinate": 8, "Y-coordinate": 1}
        actual = which_boss(character)
        expected = 3
        self.assertEqual(expected, actual)

    def test_boss_4(self):
        character = {"X-coordinate": 8, "Y-coordinate": 23}
        actual = which_boss(character)
        expected = 4
        self.assertEqual(expected, actual)
