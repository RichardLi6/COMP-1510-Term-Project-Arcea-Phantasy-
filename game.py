"""
Richard Maceda
A01378156
Richard Li
"""
from random import *




def simple_game():
    print("Hello World, Overwrite this game introduction")
    chosen_character = choose_character()
    character = make_character(chosen_character)
    rows = 10
    cols = 10
    board = make_board(rows, cols)
    describe_current_location(rows, cols, board, character)
    while True:
        direction = get_user_choice()
        # print(direction)
        valid_move = validate_move(rows, cols, character, direction, board)
        # print(valid_move)
        if valid_move:
            move_character(direction, character, board)
            describe_current_location(rows, cols, board, character)
            continue


def main():
    """
    run the game :
    """
    pass


if __name__ == "__main__":
    main()
