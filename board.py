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
    :param col: an integer representing the col in game
    :param board: a dictionary representing the coordinate values
    :character: a dictionary representing the user character stats
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


def main():
    pass


if __name__ == "__main__":
    main()
