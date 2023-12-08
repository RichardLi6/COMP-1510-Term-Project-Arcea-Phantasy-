"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
# Built-in Module
from random import *
import character as char
import random_event
import battle
import goals

# Non-Built In Module
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)


def describe_current_location(row, col, board, character):
    print(f"\n{Back.BLACK}{chr(0x2554)}{chr(0x2550) * 176}{chr(0x2557)}")

    for x in range(row):
        print(f"{chr(0x2551)}{Back.BLACK}{Fore.LIGHTWHITE_EX}{'       ' * 25} {chr(0x2551)}")
        print(f"{chr(0x2551)}", end="")

        for y in range(col):

            if x == character["X-coordinate"] and y == character["Y-coordinate"]:
                print(f"{Back.BLACK}{Fore.LIGHTWHITE_EX}| {Fore.RESET}{Fore.LIGHTYELLOW_EX} {chr(0x25A0)} {Fore.RESET}"
                      f"{Fore.LIGHTWHITE_EX} |{Fore.RESET}", end="")

            else:
                print(board[(x, y)], end="")

        print(f"{Back.BLACK}{Fore.LIGHTWHITE_EX} {chr(0x2551)}")

    print(f"{chr(0x2551)}{Back.BLACK}{Fore.WHITE}{'       ' * 25} {Fore.LIGHTWHITE_EX}{chr(0x2551)}")
    print(f"{Back.BLACK}{Fore.LIGHTWHITE_EX}{chr(0x255A)}{chr(0x2550) * 176}{chr(0x255D)}{Back.RESET}\n")


# Makes the Board
def make_board(rows, columns):
    """
    Creates a dictionary representing the ASCII art game board.

    :param rows: an integer representing the number of rows in the board
    :param columns: an integer representing the number of columns of the board
    :precondition: rows must be greater than or equal to 2
    :precondition: columns must be greater or equal to than 2
    :post-condition: creates a dictionary representing an ASCII art game board with dimensions rows x columns
    :return: the ASCII map of the game board
    """
    game_board = {}

    # Shorter way of stop use of color
    stop = Fore.RESET
    tree = "4"
    for x in range(rows):
        for y in range(columns):
            space = "|     |"
            tree = f"| {Fore.LIGHTGREEN_EX} * {stop} |"

            if randint(1, 2) == 2:
                game_board[(x, y)] = f"{Back.BLACK}{Fore.LIGHTWHITE_EX}{tree}{Back.RESET}{stop}"

            else:
                game_board[(x, y)] = f"{Back.BLACK}{Fore.LIGHTWHITE_EX}{space}{Back.RESET}{stop}"

    # Semi Boss
    game_board[(1, 1)] = f"{Back.BLACK}{Fore.LIGHTWHITE_EX}| {Fore.LIGHTBLUE_EX} ? {stop} |{Back.RESET}{stop}"
    game_board[(1, 23)] = f"{Back.BLACK}{Fore.LIGHTWHITE_EX}| {Fore.LIGHTYELLOW_EX} ??{stop} |{Back.RESET}{stop}"
    game_board[(8, 1)] = f"{Back.BLACK}{Fore.LIGHTWHITE_EX}| {Fore.LIGHTCYAN_EX}???{stop} |{Back.RESET}{stop}"
    game_board[(8, 23)] = f"{Back.BLACK}{Fore.LIGHTWHITE_EX}| {Fore.LIGHTMAGENTA_EX}???{stop} |{Back.RESET}{stop}"

    # Final Boss
    sun = chr(0x2302) + chr(0x03C6) + chr(0x2302)

    game_board[(4, 13)] = f"{Back.BLACK}{Fore.LIGHTWHITE_EX}| {Fore.LIGHTRED_EX}{sun}{stop} |{Back.RESET}{stop}"
    game_board[(4, 12)] = f"{Back.BLACK}{Fore.LIGHTWHITE_EX}| {Fore.LIGHTRED_EX}{sun}{stop} |{Back.RESET}{stop}"
    game_board[(5, 13)] = f"{Back.BLACK}{Fore.LIGHTWHITE_EX}| {Fore.LIGHTRED_EX}{sun}{stop} |{Back.RESET}{stop}"
    game_board[(5, 12)] = f"{Back.BLACK}{Fore.LIGHTWHITE_EX}| {Fore.LIGHTRED_EX}{sun}{stop} |{Back.RESET}{stop}"

    game_board["Level"] = 1

    if rows < 2 or columns < 2:
        raise Exception("Sorry no numbers below 2")

    return game_board


# Prompts the user for Direction
def get_user_choice():
    available_choices = {"1": "north", "2": "east", "3": "west", "4": "south"}

    while True:
        user_choice = input(f"\n{chr(0x2554)}{chr(0x2550) * 45}{chr(0x2557)}\n"
                            f"{chr(0x2551)}   Pick a number representing the direction  {chr(0x2551)}\n"
                            f"{chr(0x2551)}{' ' * 45}{chr(0x2551)}\n"
                            f"{chr(0x2551)}{Fore.LIGHTBLUE_EX}    1 = North  {' ' * 30}{Fore.RESET}{chr(0x2551)}\n"
                            f"{chr(0x2551)}{Fore.LIGHTYELLOW_EX}    2 = East   {' ' * 30}{Fore.RESET}{chr(0x2551)}\n"
                            f"{chr(0x2551)}{Fore.LIGHTCYAN_EX}    3 = West   {' ' * 30}{Fore.RESET}{chr(0x2551)}\n"
                            f"{chr(0x2551)}{Fore.LIGHTMAGENTA_EX}    4 = South  {' ' * 30}{Fore.RESET}{chr(0x2551)}\n"
                            f"{chr(0x255A)}{chr(0x2550) * 45}{chr(0x255D)}\n"
                            "Type number of corresponding action: \n").strip()

        if user_choice in list(available_choices.keys()):
            return available_choices[user_choice]

        else:
            print("Please enter a number that corresponds to a direction")


# Validates the move of the user
def validate_move(rows, columns, character, direction, board):
    directions = {"north": -1, "south": 1, "east": 1, "west": -1}

    if direction == "north" or direction == "south":
        to_be_y_coordinate = character["X-coordinate"] + directions[direction]

        if to_be_y_coordinate < 0 or to_be_y_coordinate == rows:
            describe_current_location(rows, columns, board, character)
            print("You cannot go there")
            return False

        else:
            return True

    if direction == "west" or direction == "east":
        to_be_x_coordinate = character["Y-coordinate"] + directions[direction]

        if to_be_x_coordinate < 0 or to_be_x_coordinate == columns:
            describe_current_location(rows, columns, board, character)
            print("You cannot go there")
            return False

        else:
            return True


# Will move the character based on the direction
def move_character(direction, character):
    direction_keys = {"north": (0, -1), "east": (1, 0), "south": (0, 1), "west": (-1, 0)}
    character["Y-coordinate"] += direction_keys[direction][0]
    character["X-coordinate"] += direction_keys[direction][1]


# Checks whether the character is alive
def is_alive(character):
    if character["Health"][0] <= 0:
        return False

    else:
        return True


# Main game
def simple_game():

    print("\n\n\nHello World, Overwrite this game introduction")

    chosen_character = char.choose_character()
    character = char.make_character(chosen_character)
    rows = 10
    cols = 25
    board = make_board(rows, cols)
    describe_current_location(rows, cols, board, character)

    while is_alive(character):
        direction = get_user_choice()
        valid_move = validate_move(rows, cols, character, direction, board)

        if valid_move:
            move_character(direction, character)
            describe_current_location(rows, cols, board, character)
            goals.semi_boss_stage(character, board)
            monster = battle.generate_monster()
            you_encountered_a_foe = random_event.random_encounter(monster, character, board)

            if you_encountered_a_foe and is_alive(character):
                battle.fight(character, monster)
                print("Sheesh")

            else:
                describe_current_location(rows, cols, board, character)
                print("This is the else block")

            char.level_up(character, chosen_character)
            goals.check_if_ready_for_final_boss(character)


def main():
    """
    run the game :
    """
    simple_game()
    pass


if __name__ == "__main__":
    main()
