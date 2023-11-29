"""
Richard Maceda
A01378156
Richard Li
A00995183
"""

from random import *
from character import *


def level_up(character, chosen_character):
    if (character["Level"] == 1) and (character["Experience"] >= 50):
        character["Level"] += 1
        if chosen_character == "Warrior":
            character["Health"] += 15
            character["Attack"] += 6
            character["Experience"] -= 50
        if chosen_character == "Ranger":
            character["Health"] += 12
            character["Attack"] += 5
            character["Experience"] -= 50
        if chosen_character == "Mage":
            character["Health"] += 10
            character["Attack"] += 8
            character["Experience"] -= 50
    elif (character["Level"] == 2) and (character["Experience"] >= 65):
        character["Level"] += 1
        if chosen_character == "Warrior":
            character["Health"] += 15
            character["Attack"] += 6
            character["Experience"] -= 65
        if chosen_character == "Ranger":
            character["Health"] += 12
            character["Attack"] += 5
            character["Experience"] -= 65
        if chosen_character == "Mage":
            character["Health"] += 10
            character["Attack"] += 8
            character["Experience"] -= 65
    elif (character["Level"] == 3) and (character["Experience"] >= 90):
        character["Level"] += 1
        if chosen_character == "Warrior":
            character["Health"] += 15
            character["Attack"] += 6
            character["Experience"] -= 90
        if chosen_character == "Ranger":
            character["Health"] += 12
            character["Attack"] += 5
            character["Experience"] -= 90
        if chosen_character == "Mage":
            character["Health"] += 10
            character["Attack"] += 8
            character["Experience"] -= 90
    elif (character["Level"] == 4) and (character["Experience"] >= 110):
        character["Level"] += 1
        if chosen_character == "Warrior":
            character["Health"] += 15
            character["Attack"] += 6
            character["Experience"] -= 110
        if chosen_character == "Ranger":
            character["Health"] += 12
            character["Attack"] += 5
            character["Experience"] -= 110
        if chosen_character == "Mage":
            character["Health"] += 10
            character["Attack"] += 8
            character["Experience"] -= 110
    elif (character["Level"] == 5) and (character["Experience"] >= 135):
        if chosen_character == "Warrior":
            character["Health"] += 15
            character["Attack"] += 6
            character["Experience"] -= 135
        if chosen_character == "Mage":
            character["Health"] += 10
            character["Attack"] += 8
            character["Experience"] -= 135
        if chosen_character == "Ranger":
            character["Health"] += 12
            character["Attack"] += 5
            character["Experience"] -= 135
            character["Dodge"] += 10
        if chosen_character == "Mage":
            character["Health"] += 10
            character["Attack"] += 8
            character["Experience"] -= 135

    pass


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

    game_board["Level"] = 1

    if rows < 2 or columns < 2:
        raise Exception("Sorry no numbers below 2")

    return game_board


def get_user_choice():
    available_choices = {"1": "north", "2": "east", "3": "south", "4": "west"}
    while True:
        user_choice = input("\n Pick a Direction\n"
                            "|-----------------------------|\n"
                            "|    1. North                 |\n"
                            "|    2. East                  |\n"
                            "|    3. South                 |\n"
                            "|    4. West                  |\n"
                            "|-----------------------------|\n").strip()

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


def generate_monster(random_number):
    monster_stats_beginner = {
        1: {"Name": "Slime", "Health": 40, "Attack": 5},
        2: {"Name": "Undead", "Health": 70, "Attack": 3},
        3: {"Name": "Imp", "Health": 40, "Attack": 7}
    }

    monster = monster_stats_beginner[random_number]
    return monster


def monster_attack(character, monster):
    character["Health"] -= monster["Attack"]
    print(f"The monster attack you for {monster["Attack"]} leaving you with {character["Health"]} health \n")
    return


def random_encounter():
    random_number = randint(1, 4)
    if random_number == 3 or random_number == 2:
        print("You encountered an enemy! ")
        print()
        return fight_or_flee(random_number)
    else:
        return False


def fight_or_flee(random_number):
    monster = generate_monster(random_number)
    while True:
        user_input = input(f"You encountered a wild {monster["Name"]}\n"
                           f"What do you want to do?.\n"
                           "|---------------------------------|\n"
                           "|    1. fight                     |\n"
                           "|    2. flee?                     |\n"
                           "|---------------------------------|\n"
                           "").strip()
        if user_input != "1" and user_input != "2":
            print("Please type either 1 or 2")
            continue
        elif user_input == "1":
            return True
        else:
            return False


def fight_with_skill(character, monster):

    index = 1

    for skill in character["Skill"].values():
        print(f"{index} Skill: {skill[0]}  Damage: {skill[1]} Mana Cost: {skill[2]}")
        index += 1

    while True:
        try:
            user_choose_skill = int(input(f"| What skill do you want to use | "))
            print()
        except ValueError:
            print("Please enter a number corresponding to skill")
            continue
        else:
            break

    chosen_skill_name = character["Skill"][user_choose_skill][0]
    chosen_skill_damage = character["Skill"][user_choose_skill][1]
    chosen_skill_mana_cost = character["Skill"][user_choose_skill][2]

    if character["Mana"] < chosen_skill_mana_cost:

        print(f"You need more Mana to cast {chosen_skill_name}")
        print()
        return
    else:
        character["Mana"] -= chosen_skill_mana_cost
        print(f"You started casting {chosen_skill_name}")
        monster["Health"] -= chosen_skill_damage

    if monster["Health"] <= 0:
        return
    else:
        print(f"{chosen_skill_name} hit the monster for {chosen_skill_damage} "
              f"leaving its Health {monster["Health"]}")
        print()
        monster_attack(character, monster)
        return


def is_alive(character):
    if character["Health"] <= 0:
        return False
    else:
        return True


def fight(character):
    monster = {"Health": 100, "Attack": 3}
    user_choices = ("1", "2", "3")

    print("You encountered a monster")
    print()
    print(f"Current Monster Health: {monster["Health"]}")

    while character["Health"] >= 0 and monster["Health"] >= 0:

        user_input = input("           What is your move?\n"
                           "|----------------------------------------|\n"
                           "|    1 Normal Attack                     |\n"
                           "|    2 Skill Skill                       |\n"
                           "|    3 Flee:                             |\n"
                           "|----------------------------------------|\n")

        if user_input not in user_choices:
            print("Please choose a number from the choices given")
            print()

        if user_input == "3":
            print(f"You successfully Flee you coward")
            return
        elif user_input == "1":
            monster["Health"] -= character["Attack"]
            if monster["Health"] <= 0:
                break
            else:
                print(f"You slashed and hit the monster for {character["Attack"]} leaving its Health {monster["Health"]}")
                print()
                monster_attack(character, monster)
        else:
            print("This is your available mana")
            print(character["Mana"])
            print()
            fight_with_skill(character, monster)
            character["Mana"] += 10
            character["Health"] += (character["Health"] + 25) % 30

    if not is_alive(character):
        print("You died Lmao")
        return
    else:
        print(f"You defeated the monster")


def simple_game():
    print("Hello World, Overwrite this game introduction")
    chosen_character = choose_character()
    character = make_character(chosen_character)
    rows = 10
    cols = 10
    board = make_board(rows, cols)
    describe_current_location(rows, cols, board, character)
    while is_alive(character):
        direction = get_user_choice()
        # print(direction)
        valid_move = validate_move(rows, cols, character, direction, board)
        # print(valid_move)
        if valid_move:
            move_character(direction, character, board)
            describe_current_location(rows, cols, board, character)
            you_encountered_a_random_entity = random_encounter()
            if you_encountered_a_random_entity and is_alive(character):
                fight(character)
                print("Sheesh")

            else:
                describe_current_location(rows, cols, board, character)
                continue


def main():
    """
    run the game :
    """
    simple_game()
    pass


if __name__ == "__main__":
    main()
