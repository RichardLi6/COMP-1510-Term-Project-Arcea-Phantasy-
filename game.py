"""
Richard Maceda
A01378156
Richard Li
A00995183
"""

from random import *
import character as char
import random_event as re
import battle


def describe_current_location(row, col, board, character):
    # listOfValues = list(board.values())[0]
    # print()
    # print(listOfValues[0])
    # print(board) #kani tung mag pakita og taas na coordinate ----------------------------- coords
    for x in range(row):
        print(" --- "*10)
        for y in range(col):
            if x == character["X-coordinate"] and y == character["Y-coordinate"]:
                board[(x, y)] = "| # |"
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
        user_choice = input("\nPick a number representing the direction\n"
                            "|----------------------------------------|\n"
                            "|    1 = North                           |\n"
                            "|    2 = East                            |\n"
                            "|    3 = South                           |\n"
                            "|    4 = West                            |\n"
                            "|----------------------------------------|\n").strip()

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


def is_alive(character):
    if character["Health"][0] <= 0:
        return False
    else:
        return True


def in_special_coordinates(character, board):
    print("You have reached one of the four pillars of this stage")
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 1 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 8 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 1 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 8 and board["Level"] == 1:
        return True
    return False


def which_boss(character):
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 1:
        return 1
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 8:
        return 2
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 1:
        return 3
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 8:
        return 4


def achieved_goal(character, board):
    if in_special_coordinates(character, board):
        if board["Level"] == 1:
            level_1_bosses = {
                1: {"Name": "North Pillar: Black Tortoise", "Health": 700, "Attack": (10, 20), "Dodge": 0,
                    "Experience": 300},
                2: {"Name": "East Pillar: Azure Dragon", "Health": 550, "Attack": (15, 35), "Dodge": 10,
                    "Experience": 300},
                3: {"Name": "West Pillar: White Tiger", "Health": 400, "Attack": (15, 35), "Dodge": 20,
                    "Experience": 300},
                4: {"Name": "South Pillar: Vermilion Bird", "Health": 500, "Attack": (20, 30), "Dodge": 10,
                    "Experience": 300}
            }
            boss = which_boss(character)
            battle.fight(character, level_1_bosses[boss])
            if level_1_bosses[1]['Health'] <= 0:
                print("You defeated one of the 4 pillars")
            elif level_1_bosses[1]['Health'] >= 0 and character['Health'][0] > 0:
                print("You successfully run from the Pillar Boss")
            else:
                print("You died try, again next time")
    else:
        return


def simple_game():
    print("Hello World, Overwrite this game introduction")
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
            achieved_goal(character, board)
            monster = battle.generate_monster()
            you_encountered_a_foe = re.random_encounter(monster, character)
            if you_encountered_a_foe and is_alive(character):
                battle.fight(character, monster)
                print("Sheesh")

            else:
                continue


def main():
    """
    run the game :
    """
    simple_game()
    pass


if __name__ == "__main__":
    main()
