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
