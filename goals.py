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
def fight_the_boss(character, boss):
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
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 1 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 23 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 1 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 23 and board["Level"] == 1:
        return True
    return False


# Determines Which semi Boss Coordinate You are on
def which_boss(character):
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 1:
        return 1
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 23:
        return 2
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 1:
        return 3
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 23:
        return 4


# Function for Semi Boss before Final Boss
def semi_boss_stage(character, board):
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
                fight_the_boss(character, level_1_bosses[boss])

    else:
        return


def check_if_ready_for_final_boss(character):
    if sorted([1, 2, 3, 4]) == sorted(character["Goal"]):
        print(f"{Fore.LIGHTYELLOW_EX}A Voice whispers above the clouds")
        print(f"{Fore.LIGHTYELLOW_EX}You are ready to face the final boss and return to Earth")
        print(f"You will see him in the {Fore.LIGHTGREEN_EX}middle of Terra")


def fight_final_boss(character):
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
