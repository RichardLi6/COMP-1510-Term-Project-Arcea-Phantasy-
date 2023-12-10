"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from unittest import TestCase
from unittest.mock import patch
from battle import try_to_flee_successfully


class TestTryToFleeSuccessfully(TestCase):
    @patch('battle.randint', return_value=1)
    def test_not_flee_successfully(self, _):
        character = {"Health": [50, 50]}
        actual = try_to_flee_successfully(character)
        expected = True
        self.assertEqual(expected, actual)

    @patch('battle.randint', return_value=2)
    def test_flee_successfully(self, _):
        character = {"Health": [50, 50]}
        actual = try_to_flee_successfully(character)
        expected = False
        self.assertEqual(expected, actual)
