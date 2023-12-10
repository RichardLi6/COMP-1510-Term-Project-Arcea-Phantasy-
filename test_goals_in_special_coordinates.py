"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from unittest import TestCase
from goals import in_special_coordinates


class TestInSpecialCoordinates(TestCase):

    def test_not_special(self):
        board = {"Level": 1}
        character = {"X-coordinate": 4, "Y-coordinate": 4}
        actual = in_special_coordinates(character, board)
        expected = False
        self.assertEqual(expected, actual)

    def test_boss_1(self):
        board = {"Level": 1}
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = in_special_coordinates(character, board)
        expected = True
        self.assertEqual(expected, actual)

    def test_boss_2(self):
        board = {"Level": 1}
        character = {"X-coordinate": 8, "Y-coordinate": 23}
        actual = in_special_coordinates(character, board)
        expected = True
        self.assertEqual(expected, actual)

    def test_boss_3(self):
        board = {"Level": 1}
        character = {"X-coordinate": 8, "Y-coordinate": 1}
        actual = in_special_coordinates(character, board)
        expected = True
        self.assertEqual(expected, actual)

    def test_boss_4(self):
        board = {"Level": 1}
        character = {"X-coordinate": 8, "Y-coordinate": 23}
        actual = in_special_coordinates(character, board)
        expected = True
        self.assertEqual(expected, actual)
