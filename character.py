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
                    "Experience": 0, "Inventory": [], "Weapon": {}, "Armor": {}, "Level": 1, "Dodge": 10,
                    "Skill": {1: ("Double Slash", 10, 10), 2: ("Vertical Slash", 15, 20)}},
        "Ranger": {"Health": [25, 25], "Attack": 5, "Mana": [60, 60], "X-coordinate": 0, "Y-coordinate": 0,
                   "Experience": 0, "Inventory": [], "Weapon": {}, "Armor": {}, "Level": 1, "Dodge": 10,
                   "Skill": {1: ("Arrow Shot", 10, 10), 2: ("Quick Slash", 15, 20)}},
        "Mage": {"Health": [20, 20], "Attack": 8, "Mana": [80, 80], "X-coordinate": 0, "Y-coordinate": 0,
                 "Experience": 0, "Inventory": [], "Weapon": {}, "Armor": {}, "Level": 1, "Dodge": 10,
                 "Skill": {1: ("Fireball", 10, 10), 2: ("Earth Fissure", 15, 20)}}
    }

    return character_stats[character]


def main():
    pass


if __name__ == "__main__":
    main()
