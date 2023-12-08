"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
import battle
import game

# Non Built In Modules
import colorama
from colorama import Fore
colorama.init(autoreset=True)


# Checks if Current Boss is Alive to prevent Exp farming abuse
def check_if_boss_is_alive(character, boss):
    """
    function checks if boss is alive

    :param character: a dictionary of the character
    :param boss: a dictionary of a boss
    :precondition: character must be a dictionary containing the user's character values
    :precondition: character must be a dictionary containing the encountered boss values
    :post-condition: prevents users from fighting the boss again
    :return: return Boolean True if boss is still alive otherwise Boolean Falls
    """
    if 1 in character["Goal"] and character["X-coordinate"] == 1 and character["Y-coordinate"] == 1:
        print(f"{Fore.LIGHTYELLOW_EX}You already defeated {Fore.LIGHTBLUE_EX}{boss['Name']} ")
        return False

    if 2 in character["Goal"] and character["X-coordinate"] == 1 and character["Y-coordinate"] == 23:
        print(f"{Fore.LIGHTYELLOW_EX}You already defeated {boss['Name']} ")
        return False

    if 3 in character["Goal"] and character["X-coordinate"] == 8 and character["Y-coordinate"] == 1:
        print(f"{Fore.LIGHTYELLOW_EX}You already defeated {Fore.LIGHTCYAN_EX}{boss['Name']} ")
        return False

    if 4 in character["Goal"] and character["X-coordinate"] == 8 and character["Y-coordinate"] == 23:
        print(f"{Fore.LIGHTYELLOW_EX}You already defeated {Fore.LIGHTMAGENTA_EX}{boss['Name']} ")
        return False

    return True


# Initiates Fight with the Boss
def fight_the_semi_boss(character, boss):
    """
    functions runs the fight against a semi boss

    :param character: a dictionary of the character
    :param boss: a dictionary of a boss
    :precondition: character must be a dictionary containing the user's character values
    :precondition: character must be a dictionary containing the encountered boss values
    :post-condition: Let character fight the boss
    :post-condition: While end the function if Character dies
    """
    battle.fight(character, boss)

    if boss['Health'] <= 0:
        character["Goal"].append(boss["ID"])
        print(f"You defeated {Fore.LIGHTYELLOW_EX}{boss['Name']}")
        print("You defeated one of the 4 Pillars")
        print(character["Goal"])

    elif boss['Health'] >= 0 and character['Health'][0] > 0:
        print("You successfully run from the Pillar Boss")

    else:
        print("You died try, again next time")


# Checks if you are in a semi boss stage
def in_special_coordinates(character, board):
    """
    function checks if character is in special coordinates

    :param board: a dictionary of the board
    :param character: a dictionary of the character
    :precondition: board must be a dictionary containing the coordinate values of the game board
    :precondition: character must be a dictionary containing the user's character values
    :post-condition: checks if character is in a special coordinate
    :return: return Boolean True if in a special coordinate otherwise Boolean False
    """
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 1 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 23 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 1 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 23 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 4 and character["Y-coordinate"] == 13 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 4 and character["Y-coordinate"] == 12 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 5 and character["Y-coordinate"] == 13 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 5 and character["Y-coordinate"] == 12 and board["Level"] == 1:
        return True
    return False


# Determines Which semi Boss Coordinate You are on
def which_boss(character):
    """
    function checks which boss is character fighting

    :param character: a dictionary of the character
    :precondition: character must be a dictionary containing the user's character values
    :post-condition: checks which boss the character is fighting if in a special tile
    :return: return a number corresponding to id of the boss character encountered
    """
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 1:
        return 1
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 23:
        return 2
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 1:
        return 3
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 23:
        return 4


# Function for Semi Boss before Final Boss
def is_character_in_boss_tile(character, board):
    """
    run the fight against semi boss

    :param board: a dictionary of the board
    :param character: a dictionary of the character
    :precondition: board must be a dictionary containing the coordinate values of the game board
    :precondition: character must be a dictionary containing the user's character values
    :post-condition: run the whole fight of the semi boss
    :post-condition: if character choose to flee fight will stop
    :post-condition: upon fleeing the boss health will restore to its max
     """
    if in_special_coordinates(character, board):
        if board["Level"] == 1:
            level_1_bosses = {
                1: {"Name": "North Pillar: Black Tortoise", "Health": 500, "Attack": (10, 21), "Dodge": 0,
                    "Experience": 300, "ID": 1},
                2: {"Name": "East Pillar: Azure Dragon", "Health": 550, "Attack": (13, 27), "Dodge": 10,
                    "Experience": 300, "ID": 2},
                3: {"Name": "West Pillar: White Tiger", "Health": 600, "Attack": (18, 38), "Dodge": 10,
                    "Experience": 300, "ID": 3},
                4: {"Name": "South Pillar: Vermilion Bird", "Health": 700, "Attack": (20, 46), "Dodge": 20,
                    "Experience": 300, "ID": 4},
            }

            boss = which_boss(character)

            if not check_if_boss_is_alive(character, level_1_bosses[boss]):
                print(f"Prepare and Find the Other Pillars")

            else:
                print("You have reached one of the four pillars of this stage")
                fight_the_semi_boss(character, level_1_bosses[boss])

    else:
        return


# Checks if character is ready for final boss and informs the player
def check_if_ready_for_final_boss(character):
    """
    function checks if ready for final boss

    :param character: a dictionary of the character
    :pre-condition: must be dictionary containing the user's character values
    :post-condition: add key and value of Final Boss: True to allow character to access final stage
    """
    if sorted([1, 2, 3, 4]) == sorted(character["Goal"]):
        character["Final Boss"] = True
        print(character)


# Final Boss Fight which is slightly different from a normal fight
def fight_final_boss(character):
    """
    run the fight against final boss

    :param character: a dictionary
    :precondition: character must be a dictionary containing the user's character values
    :post-condition: run the whole fight of the final boss
    :post-condition: game will end once the boss is dead
    """
    boss = {
        "Name": "Demon Lord", "Health": 1000, "Attack": (45, 90),
        "Skills": ("Battle Cry", "Brace", "Inferno Blasy")
               }
    user_choices = ("1", "2", "3", "4")

    while character["Health"][0] >= 0 and boss["Health"] > 0:

        user_input = battle.user_prompt()

        if user_input not in user_choices:
            print("Please choose a number from the choices given")
            continue

        if user_input == "4":

            if battle.try_to_flee_successfully(character):
                return

            else:
                continue

        elif user_input == "1":
            boss["Health"] -= character["Attack"]

            if boss["Health"] <= 0:
                break

            else:
                battle.normal_attack_description(character)
                battle.monster_attack(character, boss)

        elif user_input == "3":
            print("The monster was a tad bit faster than you ")
            battle.monster_attack(character, boss)
            battle.heal_character(character)

        else:
            battle.fight_with_skill(character, boss)
            battle.monster_attack(character, boss)

        if game.is_alive(character):
            battle.passive_regeneration(character)

        else:
            break

    if not game.is_alive(character):
        print("You died Lmao")
        return

    else:
        print("You Defeated the Last Boss ")
        print("Suddenly you wake up noticing you still have Exams coming for 1510")


def main():
    pass


if __name__ == "__main__":
    main()
