"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
import colorama
from colorama import Fore
colorama.init(autoreset=True)


# Initialize Character from User Prompt
def make_character(character):
    """
    Creates a game character.

    Game character contains stats and attributes listed in function.

    :param character: a string containing character information
    :precondition: character must be one of the keys of the dictionary
    :post-condition: creates dictionary containing the stats of the game character.
    :return: returns the dictionary of character stats
    """
    character_stats = {
        "Warrior": {
            "Class": "Warrior",
            "Health": [50, 50],
            "Attack": 9,
            "Mana": [60, 60],
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Experience": 0,
            "Inventory": [],
            "Weapon": {},
            "Armor": {},
            "Level": 1,
            "Dodge": 10,
            "Goal": [],
            "Final Boss": False,
            "Skill": {
                1: ("Double Slash", 10, 10)
            }
        },
        "Ranger": {
            "Class": "Ranger",
            "Health": [50, 50],
            "Attack": 9,
            "Mana": [60, 60],
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Experience": 0,
            "Inventory": [],
            "Weapon": {},
            "Armor": {},
            "Level": 1,
            "Dodge": 10,
            "Goal": [],
            "Final Boss": False,
            "Skill": {
                1: ("Arrow Shot", 10, 10)
            }
        },
        "Mage": {
            "Class": "Mage",
            "Health": [40, 40],
            "Attack": 9,
            "Mana": [80, 80],
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Experience": 0,
            "Inventory": [],
            "Weapon": {},
            "Armor": {},
            "Level": 1,
            "Dodge": 10,
            "Goal": [],
            "Final Boss": False,
            "Skill": {
                1: ("Fireball", 15, 10)
            }
        }
    }

    return character_stats[character]


# Prompt User for Choice of Class
def choose_character():
    valid_answers = {"1": "Warrior", "2": "Ranger", "3": "Mage"}
    while True:
        user_class = input(f"{chr(0x2554)}{chr(0x2550) * 40}{chr(0x2557)}\n"
                           f"{chr(0x2551)}{' ' * 12}  Pick a Class: {' ' * 12}{chr(0x2551)}\n"
                           f"{chr(0x2551)}{Fore.LIGHTYELLOW_EX}   1 = Warrior {' ' * 25}{Fore.RESET}{chr(0x2551)}\n"
                           f"{chr(0x2551)}{Fore.LIGHTGREEN_EX}   2 = Ranger {' ' * 26}{Fore.RESET}{chr(0x2551)}\n"
                           f"{chr(0x2551)}{Fore.LIGHTMAGENTA_EX}   3 = Mage {' ' * 28}{Fore.RESET}{chr(0x2551)}\n"
                           f"{chr(0x255A)}{chr(0x2550) * 40}{chr(0x255D)}\n"
                           "Type number of Chosen Class: \n")

        if user_class not in valid_answers:
            print("Please type in a number corresponding to the chosen class")
            continue
        else:
            return valid_answers[user_class]


# Increased Stats for Level Up
def increased_stats(character, character_class):
    """
    Increase character stats upon level up.

    :param character: the dictionary of character stats
    :param character_class: user input of chosen character
    :precondition: user must have chosen a character
    :precondition: character must have enough experience to level up
    :post-condition: character stats increase upon level up
    """
    stat_increases = {
        "Warrior": {"Health": 25, "Attack": 7, "Mana": 20},
        "Ranger": {"Health": 20, "Attack": 6, "Mana": 25},
        "Mage": {"Health": 15, "Attack": 5, "Mana": 30}
    }

    character["Health"][1] += stat_increases[character_class]["Health"]
    character["Mana"][1] += stat_increases[character_class]["Mana"]
    character["Attack"] += stat_increases[character_class]["Attack"]


# New Skills
def new_skills(character, character_class):
    """
    function adds new character skill base on class

    :param character: a dictionary representing user character stats
    :param character_class: a string representing user character's class
    :precondition: only appends skill once character reaches a specific level
    :post-condition: appends character skills key with a new skill
    """
    if character_class == "Warrior":
        warrior_skills = {
            2: ("Vertical Slash", 15, 20),
            3: ("Riptide Slash", 25, 30),
            4: ("Brutal Cleave", 45, 50),
            5: ("Double Avant", 65, 80),
            6: ("Cataclysmic Onslaught", 100, 120)
        }
        current_level = character["Level"]
        character["Skill"][current_level] = warrior_skills[current_level]

    if character_class == "Ranger":
        ranger_skills = {
            2: ("Quick Slash", 15, 20),
            3: ("Eagles Wrath", 30, 10),
            4: ("Forest Sprint", 25, 30),
            5: ("Celestial Precision", 50, 90),
            6: ("Nature's Retribution", 95, 120)
        }
        current_level = character["Level"]
        character["Skill"][current_level] = ranger_skills[current_level]

    if character_class == "Mage":
        mage_skills = {
            2: ("Earth Fissure", 20, 20),
            3: ("Frost Nova", 35, 45),
            4: ("Chain Lightning", 50, 60),
            5: ("Solar Flare", 75, 100),
            6: ("Ethereal Cataclysm", 100, 150)
        }
        current_level = character["Level"]
        character["Skill"][current_level] = mage_skills[current_level]


# Leveling Up System
def level_up(character, chosen_character):
    """
    Increase character stats upon level up.

    :param character: the dictionary of character stats
    :param chosen_character: user input of chosen character
    :precondition: user must have chosen a character
    :precondition: character must have enough experience to level up
    :post-condition: character stats increase upon level up
    """
    level_requirements = {1: 40, 2: 70, 3: 90, 4: 130, 5: 155, 6: 180}

    character_class = chosen_character
    current_level = character["Level"]

    if current_level == 6:
        print("Max Level no More Level Ups")
        return

    if current_level in level_requirements and character["Experience"] >= level_requirements[current_level]:
        print(f"{Fore.LIGHTYELLOW_EX}You have Level Up! ")
        character["Level"] += 1
        character["Experience"] -= level_requirements[current_level]

        increased_stats(character, character_class)
        new_skills(character, character_class)

    # Special case for Ranger at level 6, get extra Dodge
    if character_class == "Ranger" and current_level == 5:
        character["Dodge"] += 10
    # Special case for Warrior at level 5, get extra Health
    if character_class == "Warrior" and current_level == 4:
        character["Health"] += 10


def main():
    pass


if __name__ == "__main__":
    main()
