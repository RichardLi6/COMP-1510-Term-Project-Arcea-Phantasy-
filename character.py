"""
Richard Maceda
A01378156
Richard Li
A00995183
"""

# 24 25 27 + 3
def choose_character():
    valid_answers = {"1": "Warrior", "2": "Ranger", "3": "Mage"}
    while True:
        user_class = input(f"{chr(0x2554)}{chr(0x2550) * 40}{chr(0x2557)}\n"
                           f"{chr(0x2551)}{" " * 12}  Pick a Class: {" " * 12}{chr(0x2551)}\n"
                           f"{chr(0x2551)}   1 = Warrior {" " * 25}{chr(0x2551)}\n"
                           f"{chr(0x2551)}   2 = Ranger {" " * 26}{chr(0x2551)}\n"
                           f"{chr(0x2551)}   3 = Mage {" " * 28}{chr(0x2551)}\n"
                           f"{chr(0x255A)}{chr(0x2550) * 40}{chr(0x255D)}\n"
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
    level_requirements = {1: 50, 2: 65, 3: 90, 4: 110, 5: 135}
    stat_increases = {
        "Warrior": {"Health": 15, "Attack": 6},
        "Ranger": {"Health": 12, "Attack": 5},
        "Mage": {"Health": 10, "Attack": 8}
    }
    current_level = character["Level"]
    if current_level in level_requirements and character["Experience"] >= level_requirements[current_level]:
        character["Level"] += 1
        character["Experience"] -= level_requirements[current_level]

        if chosen_character in stat_increases:
            for stat, value in stat_increases[chosen_character].items():
                character[stat] += value

            # Special case for Ranger at level 6, get extra Dodge
            if chosen_character == "Ranger" and current_level == 5:
                character["Dodge"] += 10
            # Special case for Warrior at level 5, get extra Health
            if chosen_character == "Warrior" and current_level == 4:
                character["Health"] += 10


def main():
    pass


if __name__ == "__main__":
    main()
