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
import story

# Non-Built In Module
import colorama
from colorama import Style
colorama.init(autoreset=True)


# Main game
def simple_game():
    """
    collection of functions running the game
    """
    story.print_game_introduction()
    chosen_character = char.choose_character()
    character = char.make_character(chosen_character)
    rows = 10
    cols = 25
    board = b.make_board(rows, cols)
    b.describe_current_location(rows, cols, board, character)

    while battle.is_alive(character):
        print(f"{Style.RESET_ALL}")
        direction = b.get_user_choice()
        valid_move = b.validate_move(rows, cols, character, direction, board)

        if valid_move:
            b.move_character(direction, character)
            b.describe_current_location(rows, cols, board, character)
            goals.is_character_in_boss_tile(character, board)
            monster = battle.generate_monster()
            you_encountered_a_foe = random_event.random_encounter(monster, character, board)

            if you_encountered_a_foe and battle.is_alive(character):
                battle.fight(character, monster)

            else:
                print(f"{Style.RESET_ALL}")

        else:
            b.describe_current_location(rows, cols, board, character)
            print("You cannot go there")

            char.level_up(character, chosen_character)
            goals.check_if_win(character)


def main():
    """
    run the game :
    """
    simple_game()
    pass


if __name__ == "__main__":
    main()
