"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
# Built-in Module
import character as char
import random_event
import battle
import goals
import board as b


# Non-Built In Module
import colorama
from colorama import Fore
colorama.init(autoreset=True)


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
            board.describe_current_location(rows, columns, board, character)
            print("You cannot go there")
            return False

        else:
            return True

    if direction == "west" or direction == "east":
        to_be_x_coordinate = character["Y-coordinate"] + directions[direction]

        if to_be_x_coordinate < 0 or to_be_x_coordinate == columns:
            board.describe_current_location(rows, columns, board, character)
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


# Checks whether the character is alive
def is_alive(character):
    """
    function checks if user is alive

    :param character: a dictionary representing that character's stats
    :post-condition: checks the character Health Value
    :return: return False if character Health is equal to or less than zero
    :return: return True if character Health is greater than 0
    """
    if character["Health"][0] <= 0:
        return False

    else:
        return True


# Main game
def simple_game():
    """
    collection of functions running the game
    """

    print("\n\n\nHello World, Overwrite this game introduction")

    chosen_character = char.choose_character()
    character = char.make_character(chosen_character)
    rows = 10
    cols = 25
    board = b.make_board(rows, cols)
    b.describe_current_location(rows, cols, board, character)

    while is_alive(character):
        direction = get_user_choice()
        valid_move = validate_move(rows, cols, character, direction, board)

        if valid_move:
            move_character(direction, character)
            b.describe_current_location(rows, cols, board, character)
            goals.is_character_in_boss_tile(character, board)
            monster = battle.generate_monster()
            you_encountered_a_foe = random_event.random_encounter(monster, character, board)

            if you_encountered_a_foe and is_alive(character):
                battle.fight(character, monster)
                print("Sheesh")

            else:
                b.describe_current_location(rows, cols, board, character)
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
