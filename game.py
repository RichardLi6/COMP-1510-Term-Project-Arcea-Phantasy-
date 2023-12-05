"""
Richard Maceda
A01378156
Richard Li
A00995183
"""

from random import *
import character as char
import random_event
import battle
import special_tiles

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def describe_current_location(row, col, board, character):
    # listOfValues = list(board.values())[0]
    # print()
    # print(listOfValues[0])
    # print(board) #kani tung mag pakita og taas na coordinate ----------------------------- coords
    for x in range(row):
        print(" --- "*10)
        for y in range(col):
            if x == character["X-coordinate"] and y == character["Y-coordinate"]:
                board[(x, y)] = f"| {Fore.LIGHTYELLOW_EX}#{Fore.RESET} |"
                print(board[(x, y)], end="")
            else:
                print(board[(x, y)], end="")
        print()
    print(" --- " * 10)


def make_board(rows, columns):
    game_board = {}

    for x in range(rows):
        for y in range(columns):
            # space = f"|{x},{y}|"
            space = "|   |"
            if randint(1, 2) == 2:
                game_board[(x, y)] = "|   |"
            else:
                game_board[(x, y)] = f"{space}"

    game_board[(1, 1)] = f"| 1 |"
    game_board[(1, 8)] = f"| 2 |"
    game_board[(8, 1)] = f"| 3 |"
    game_board[(8, 8)] = f"| 4 |"

    game_board["Level"] = 1

    if rows < 2 or columns < 2:
        raise Exception("Sorry no numbers below 2")

    return game_board


def get_user_choice():
    available_choices = {"1": "north", "2": "east", "3": "south", "4": "west"}
    while True:
        user_choice = input(f"\n{chr(0x2554)}{chr(0x2550) * 45}{chr(0x2557)}\n"
                            f"{chr(0x2551)}   Pick a number representing the direction  {chr(0x2551)}\n"
                            f"{chr(0x2551)}{" " * 45}{chr(0x2551)}\n"
                            f"{chr(0x2551)}{Fore.LIGHTBLUE_EX}    1 = North  {" " * 30}{Fore.RESET}{chr(0x2551)}\n"
                            f"{chr(0x2551)}{Fore.LIGHTYELLOW_EX}    2 = East   {" " * 30}{Fore.RESET}{chr(0x2551)}\n"
                            f"{chr(0x2551)}{Fore.LIGHTMAGENTA_EX}    3 = South  {" " * 30}{Fore.RESET}{chr(0x2551)}\n"
                            f"{chr(0x2551)}{Fore.LIGHTCYAN_EX}    4 = West   {" " * 30}{Fore.RESET}{chr(0x2551)}\n"
                            f"{chr(0x255A)}{chr(0x2550) * 45}{chr(0x255D)}\n"
                            "Type number of corresponding action: \n").strip()

        if user_choice in list(available_choices.keys()):
            return available_choices[user_choice]
        else:
            print("Please enter a number that corresponds to a direction")


def validate_move(rows, columns, character, direction, board):
    directions = {"north": -1, "south": 1, "east": 1, "west": -1}

    if direction == "north" or direction == "south":
        to_be_y_coordinate = character["X-coordinate"] + directions[direction]

        if to_be_y_coordinate < 0 or to_be_y_coordinate == columns:
            describe_current_location(rows, columns, board, character)
            return False
        else:
            return True

    if direction == "west" or direction == "east":
        to_be_x_coordinate = character["Y-coordinate"] + directions[direction]

        if to_be_x_coordinate < 0 or to_be_x_coordinate == rows:
            describe_current_location(rows, columns, board, character)
            return False
        else:
            return True


def move_character(direction, character, board):
    direction_keys = {"north": (0, -1), "east": (1, 0), "south": (0, 1), "west": (-1, 0)}
    board[(character["X-coordinate"], character["Y-coordinate"])] = "|   |"
    character["Y-coordinate"] += direction_keys[direction][0]
    character["X-coordinate"] += direction_keys[direction][1]


def is_alive(character):
    if character["Health"][0] <= 0:
        return False
    else:
        return True


def simple_game():
    print("\n\n\nHello World, Overwrite this game introduction")
    chosen_character = char.choose_character()
    character = char.make_character(chosen_character)
    rows = 10
    cols = 10
    board = make_board(rows, cols)
    describe_current_location(rows, cols, board, character)
    while is_alive(character):
        # print(board)
        direction = get_user_choice()
        # print(direction)
        valid_move = validate_move(rows, cols, character, direction, board)
        # print(valid_move)
        if valid_move:
            move_character(direction, character, board)
            describe_current_location(rows, cols, board, character)
            special_tiles.achieved_goal(character, board)
            monster = battle.generate_monster()
            you_encountered_a_foe = random_event.random_encounter(monster, character, board)
            if you_encountered_a_foe and is_alive(character):
                battle.fight(character, monster)
                print("Sheesh")

            else:
                print("This is the else block")
            char.level_up(character, chosen_character)


def main():
    """
    run the game :
    """
    simple_game()
    pass


if __name__ == "__main__":
    main()
