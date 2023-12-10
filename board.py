"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from random import randint

# Non Built-in Modules
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)


def describe_current_location(row, col, board, character):
    """
    function shows the current location of the user

    :param row: an integer representing the rows in the game
    :param col: an integer representing the columns in game
    :param board: a dictionary representing the coordinate values
    :param character: a dictionary representing the user character stats
    :post-condition: print the user's current location
    """
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
    """
    function prompts the user what to do when not in fight

    :precondition: user will enter an infinite loop until entering a valid input
    :post-condition: prompt user for a direction to go to
    """
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
    """
    function validates the move of user

    :param rows: an integer representing the rows in the game
    :param columns: an integer representing the col in game
    :param board: a dictionary representing the coordinate values
    :param character: a dictionary representing the user character stats
    :param direction: a string representing a direction
    :post-condition: validate if the direction pass is valid
    :return: return True if direction is valid
    :return: return False if direction is invalid
    """
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
    """
    function moves the character in board

    :param direction: a string representing a direction
    :param character: a dictionary representing the user character's stats
    :pre-condition: direction must already be validated
    :post-condition: modify character's X_coordinate value and Y_coordinate corresponding to direction
    """
    direction_keys = {"north": (0, -1), "east": (1, 0), "south": (0, 1), "west": (-1, 0)}
    character["Y-coordinate"] += direction_keys[direction][0]
    character["X-coordinate"] += direction_keys[direction][1]



