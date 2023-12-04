"""
Richard Maceda
A01378156
Richard Li
A00995183
"""


def choose_character():
    valid_answers = {"1": "Warrior", "2": "Ranger", "3": "Mage"}
    while True:
        user_class = input("        Pick a Class\n"
                           "|---------------------------|\n"
                           "|    1. Warrior             |\n"
                           "|    2. Ranger              |\n"
                           "|    3. Mage                |\n"
                           "|---------------------------|\n"
                           "Type number of Chosen Class: \n")

        if user_class not in valid_answers:
            print("Please type in a number corresponding to the chosen class")
            continue
        else:
            return valid_answers[user_class]


def make_character(character):
    character_stats = {
        "Warrior": {"Health": [30, 30], "Attack": 6, "Mana": [50, 50], "X-coordinate": 0, "Y-coordinate": 0,
                    "Experience": 0, "Inventory": [], "Weapon": {}, "Armor": {}, "Level": 1, "Dodge": 10, "Goal": [],
                    "Skill": {1: ("Double Slash", 10, 10), 2: ("Vertical Slash", 15, 20)}},
        "Ranger": {"Health": [25, 25], "Attack": 5, "Mana": [60, 60], "X-coordinate": 0, "Y-coordinate": 0,
                   "Experience": 0, "Inventory": [], "Weapon": {}, "Armor": {}, "Level": 1, "Dodge": 10, "Goal": [],
                   "Skill": {1: ("Arrow Shot", 10, 10), 2: ("Quick Slash", 15, 20)}},
        "Mage": {"Health": [20, 20], "Attack": 8, "Mana": [80, 80], "X-coordinate": 0, "Y-coordinate": 0,
                 "Experience": 0, "Inventory": [], "Weapon": {}, "Armor": {}, "Level": 1, "Dodge": 10, "Goal": [],
                 "Skill": {1: ("Fireball", 10, 10), 2: ("Earth Fissure", 15, 20)}}
    }

    return character_stats[character]


def level_up(character, chosen_character):
    if (character["Level "] == 1) and (character["Experience"] >= 50):
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


def main():
    pass


if __name__ == "__main__":
    main()
