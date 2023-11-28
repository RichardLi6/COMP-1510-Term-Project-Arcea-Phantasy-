"""
A docstring
"""


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
        "Warrior": {"Health": 30, "Attack": 6, "Dodge": 10, "X-coordinate": 0, "Y-coordinate": 0, "Experience": 0,
                    "Inventory": [], "Weapon": {}, "Armor": {}, "Level": 1,
                    "Skill": {1: ("Double Slash", 10), 2: ("Vertical Slash", 15)}},
        "Ranger": {"Health": 25, "Attack": 5, "Dodge": [], "X-coordinate": 0, "Y-coordinate": 0, "Experience": 0,
                   "Inventory": [], "Weapon": {}, "Armor": {}, "Level": 1,
                   "Skill": {1: ("Arrow Shot", 10), 2: ("Quick Slash", 15) }},
        "Mage": {"Health": 20, "Attack": 8, "Dodge": [], "X-coordinate": 0, "Y-coordinate": 0, "Experience": 0,
                 "Inventory": [], "Weapon": {}, "Armor": {}, "Level": 1,
                 "Skill": {1: ("Fireball", 10), 2: ("Fissure", 15)}}
    }

    return character_stats[character]


def main():
    pass


if __name__ == "__main__":
    main()
