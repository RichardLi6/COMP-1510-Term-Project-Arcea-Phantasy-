"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from random import randint
from special_tiles import in_special_coordinates


def random_encounter(monster, character, board):

    if in_special_coordinates(character, board):
        return False

    random_number = randint(1, 4)

    if random_number == 3 or random_number == 2:
        return fight_or_flee(monster)
    else:
        return False


def fight_or_flee(monster):
    while True:
        user_input = input(f"You encountered a wild {monster['Name']}!\n"
                           f"\n{chr(0x2554)}{chr(0x2550) * 33}{chr(0x2557)}\n"
                           f"{chr(0x2551)}     What do you want to do?     {chr(0x2551)}\n"
                           f"{chr(0x2551)}                                 {chr(0x2551)}\n"
                           f"{chr(0x2551)}    1. fight                     {chr(0x2551)}\n"
                           f"{chr(0x2551)}    2. flee?                     {chr(0x2551)}\n"
                           f"{chr(0x255A)}{chr(0x2550) * 33}{chr(0x255D)}\n"
                           "").strip()
        if user_input != "1" and user_input != "2":
            print("Please type either 1 or 2")
            continue
        elif user_input == "1":
            return True
        else:
            return False


def main():
    pass


if __name__ == "__main__":
    main()
