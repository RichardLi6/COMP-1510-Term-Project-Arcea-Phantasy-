"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from board import validate_move
from unittest import TestCase


class TestValidateMove(TestCase):
    def test_valid_move(self):
        board_1 = {
            (0, 0): "| |", (1, 0): "| |", (2, 0): "| |",
            (0, 1): "| |", (1, 1): "| |", (2, 1): "| |",
            (0, 2): "| |", (1, 2): "| |", (2, 2): "| |"
        }
        row = 3
        col = 3
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = "west"
        expected_output = True
        actual_output = validate_move(row, col, character, direction, board_1)
        self.assertEqual(expected_output, actual_output)

    def test_invalid_move(self):
        board_2 = {
            (0, 0): "| |", (1, 0): "| |", (2, 0): "| |",
            (0, 1): "| |", (1, 1): "| |", (2, 1): "| |",
            (0, 2): "| |", (1, 2): "| |", (2, 2): "| |"
        }
        row = 3
        col = 3
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "west"
        expected_output = False
        actual_output = validate_move(row, col, character, direction, board_2)
        self.assertEqual(expected_output, actual_output)




