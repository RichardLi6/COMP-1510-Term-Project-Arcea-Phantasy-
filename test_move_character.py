"""
Richard Maceda
A01378156
"""
from unittest import TestCase
from board import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        move_character( "north", character)
        expected = {'X-coordinate': 0, 'Y-coordinate': 1}
        self.assertEqual(expected, character)

    def test_move_character_south(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        move_character("south", character)
        expected = {'X-coordinate': 2, 'Y-coordinate': 1}
        self.assertEqual(expected, character)

    def test_move_character_east(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        move_character("east", character)
        expected = {'X-coordinate': 1, 'Y-coordinate': 2}
        self.assertEqual(expected, character)

    def test_move_character_west(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        move_character("west", character)
        expected = {'X-coordinate': 1, 'Y-coordinate': 0}
        self.assertEqual(expected, character)
