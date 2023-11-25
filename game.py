"""
Richard Maceda
A01378156
Richard Li
"""
from random import *


def choose_character():
    valid_answers = {"1": "Warrior", "2": "Ranger", "3": "Mage"}
    while True:
        user_class = input("|---Pick a Class---|\n"
                           "| 1. Warrior       |\n"
                           "| 2. Ranger        |\n"
                           "| 3. Mage          |\n"
                           "|------------------|\n"
                           "Type number of Chosen Class: ")

        if user_class not in valid_answers:
            print("Please type in a number corresponding to the chosen class")
            continue
        else:
            return valid_answers[user_class]


def make_character(character):
    character_stats = {
        "warrior": {"Health": 30, "Attack": 6, "Dodge": [], "X-coordinate": 0, "Y-coordinate": 0, "Experience": 0,
                    "Level": 0},
        "ranger": {"Health": 25, "Attack": 5, "Dodge": [], "X-coordinate": 0, "Y-coordinate": 0, "Experience": 0,
                   "Level": 0},
        "mage": {"Health": 20, "Attack": 8, "Dodge": [], "X-coordinate": 0, "Y-coordinate": 0, "Experience": 0,
                 "Level": 0}
    }

    return character_stats[character]

def level_up(character, chosen_character):
    if (character["Level"] == 1) and (character["Experience"] >= 50):
        character["Level"] += 1
        if chosen_character == "Warrior":
            character["Health"] +=
            character["Attack"] +=
            character["Experience"] -= 50
    elif (character["Level"] == 2) and (character["Experience"] >= 65):
        character["Level"] += 1
    elif (character["Level"] == 3) and (character["Experience"] >= 90):
        character["Level"] += 1
    elif (character["Level"] == 4) and (character["Experience"] >= 110):
        character["Level"] += 1
    elif (character["Level"] == 5) and (character["Experience"] >= 135):
        character["Level"] += 1
    pass


def describe_current_location(row, col, board, character):
    # listOfValues = list(board.values())[0]
    # print()
    # print(listOfValues[0])
    print(board) #kani tung mag pakita og taas na coordinate ----------------------------- coords
    for x in range(row):
        print(" --- "*10)
        for y in range(col):
            if x == character["X-coordinate"] and y == character["Y-coordinate"]:
                board[(x, y)] = "| # |"
                print(board[(x, y)], end="")
            else:
                print(board[(x, y)], end="")
        print()



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
