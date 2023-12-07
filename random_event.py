"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from random import randint
from goals import in_special_coordinates

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def random_encounter(monster, character, board):
    """
    Encounter a random monster by chance

    :param monster: a dictionary containing a dictionary of different types of monsters and stats
    :param character: a dictionary of chosen character's stats
    :param board: a dictionary representing the ASCII art game board
    :precondition: character moves in a direction
    :postcondition: Checks for a random encounter with a monster on the game board.
    :postcondition: If a random encounter happens, player is prompt to fight or flee
    :return: True if there is a random encounter, False if there is not
    """

    if in_special_coordinates(character, board):
        return False

    random_number = randint(1, 10)

    encounter_chance = (1, 3, 9, 7,)
    if random_number in encounter_chance:
        return fight_or_flee(monster)
    else:
        return False


def fight_or_flee(monster):
    """

    Prompt user to choose to fight or flee from a monster encounter.

    :param monster: a dictionary containing a dictionary of different types of monsters and stats
    :precondition: the user encounters a monster
    :postcondition: consistently prompts user to input '1' or '2'
    :return: True if user decides to fight, False if user attempts to flee
    """
    while True:
        user_input = input(f"\nYou encountered a wild {Fore.LIGHTYELLOW_EX}{monster['Name']}!{Fore.RESET}\n"
                           f"\n{chr(0x2554)}{chr(0x2550) * 29}{chr(0x2557)}\n"
                           f"{chr(0x2551)}   What do you want to do?   {chr(0x2551)}\n"
                           f"{chr(0x2551)}                             {chr(0x2551)}\n"
                           f"{chr(0x2551)}{Fore.LIGHTYELLOW_EX}  1 = fight                  {Fore.RESET}{chr(0x2551)}\n"
                           f"{chr(0x2551)}{Fore.LIGHTGREEN_EX}  2 = flee?                  {Fore.RESET}{chr(0x2551)}\n"
                           f"{chr(0x255A)}{chr(0x2550) * 29}{chr(0x255D)}\n"
                           "Pick a number "
                           "").strip()
        if user_input != "1" and user_input != "2":
            print("Please type either 1 or 2")
            continue
        elif user_input == "1":
            return True
        else:
            return False


def main():
    pass


if __name__ == "__main__":
    main()
