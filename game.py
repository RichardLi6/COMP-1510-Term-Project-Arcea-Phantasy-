"""
Richard Maceda
A01378156
Richard Li
"""
from random import *
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

    if rows < 2 or columns < 2:
        raise Exception("Sorry no numbers below 2")

    return game_board


def get_user_choice():
    available_choices = {"1": "north", "2": "east", "3": "south", "4": "west"}
    while True:
        print("\n|-Pick a direction-|\n"
              "| 1. North         |\n"
              "| 2. East          |\n"
              "| 3. South         |\n"
              "| 4. West          |\n"
              "|------------------|\n")
        user_choice = input("Pick a direction: ").strip()

        if user_choice in list(available_choices.keys()):
            return available_choices[user_choice]
        else:
            print("Please enter a number that corresponds to a direction")
            continue


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
