"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from unittest import TestCase
from goals import check_if_win


class TestCheckIfWin(TestCase):
    def test_user_win_while_fighting_all_4_boss_in_order(self):
        character = {"Goal": [1, 2, 3, 4], "Final Boss": True}
        actual = check_if_win(character)
        expected = True

    def test_user_win_while_fighting_all_4_boss_but_not_in_order(self):
        character = {"Goal": [1, 2, 3, 4], "Final Boss": True}
        actual = check_if_win(character)
        expected = True

    def test_user_only_killed_3_boss(self):
        character = {"Goal": [1, 2, 3], "Final Boss": False}
        actual = check_if_win(character)
        expected = False

    def test_user_did_not_kill_any_boss(self):
        character = {"Goal": [1, 2, 3], "Final Boss": False}
        actual = check_if_win(character)
        expected = False
