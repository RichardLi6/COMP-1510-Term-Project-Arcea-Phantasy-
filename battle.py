"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
from random import randint
from game import is_alive

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


# Function that generates a monster
def generate_monster():
    beginner_monsters_list = {
        1: {"Name": "Slime", "Health": 60, "Attack": (4, 8), "Experience": 15},
        2: {"Name": "Undead", "Health": 80, "Attack": (3, 5), "Experience": 15},
        3: {"Name": "Imp", "Health": 45, "Attack": (5, 10), "Experience": 15}
    }

    random_number = randint(1, 3)
    monster = beginner_monsters_list[random_number]
    return monster


# Prints the introduction whenever fighting
def fight_introduction(character, monster):
    print()
    print(chr(0x2550) * 30)
    print("You:")
    print(f"Health {Fore.LIGHTGREEN_EX}{character['Health'][0]}/{character['Health'][1]}")
    print(f"Mana: {Fore.LIGHTCYAN_EX}{character['Mana'][0]}/{character['Mana'][1]}")
    print()
    print("Enemy: ")
    print(f"{Fore.LIGHTYELLOW_EX}{monster['Name']}")
    print(f"Health: {Fore.LIGHTRED_EX}{monster['Health']}")
    print(chr(0x2550) * 30)
    print()


# A Text confirmation after user wins a fight
def after_fight(character, monster):
    print()
    print((chr(0x2550) * 15) + " You defeated the monster " + (chr(0x2550) * 15))
    print()

    character["Experience"] += monster["Experience"]
    print(f"You gain: {Fore.LIGHTYELLOW_EX}{monster['Experience']} Exp {Fore.RESET}from defeating the monster")

    character["Mana"][0] = min(character["Mana"][0] + 35, character["Mana"][1])
    print(f"Your mana replenish by {Fore.LIGHTCYAN_EX}35{Fore.RESET}")

    character["Health"][0] = min(character["Health"][0] + 25, character["Health"][1])
    print(f"Your health replenish by {Fore.LIGHTGREEN_EX}25{Fore.RESET}")

    print()
    print(f"Health {Fore.LIGHTGREEN_EX}{character['Health'][0]}/{character['Health'][1]}")
    print(f"Mana: {Fore.LIGHTCYAN_EX}{character['Mana'][0]}/{character['Mana'][1]}")
    print()
    print((chr(0x2550) * 56))
    print()


# Function whenenever Character is in a fight
def fight(character, monster):
    user_choices = ("1", "2", "3")

    while character["Health"][0] >= 0 and monster["Health"] > 0:
        fight_introduction(character, monster)

        user_input = input(f"\n{chr(0x2554)}{chr(0x2550) * 27}{chr(0x2557)}\n"
                           f"{chr(0x2551)}  What do you want to do:  {chr(0x2551)}\n"
                           f"{chr(0x2551)}                           {chr(0x2551)}\n"
                           f"{chr(0x2551)}    1 = Normal Attack      {chr(0x2551)}\n"
                           f"{chr(0x2551)}    2 = Skill Attack       {chr(0x2551)}\n"
                           f"{chr(0x2551)}    3 = Flee               {chr(0x2551)}\n"
                           f"{chr(0x255A)}{chr(0x2550) * 27}{chr(0x255D)}\n"
                           "Type a number to corresponding action: \n")

        if user_input not in user_choices:
            print("Please choose a number from the choices given")
            continue

        if user_input == "3":
            print(f"You successfully Flee you coward")
            return

        elif user_input == "1":
            monster["Health"] -= character["Attack"]
            if monster["Health"] <= 0:
                break
            else:
                print(f"You slashed the monster for {Fore.WHITE}{character['Attack']}{Fore.RESET} leaving its Health {Fore.LIGHTRED_EX}{monster['Health']}")
                print()
                monster_attack(character, monster)

        else:
            fight_with_skill(character, monster)

        if is_alive(character):

            character["Mana"][0] = min(character["Mana"][0] + 5, character["Mana"][1])
            print("Your mana passively replenish by 5")

            character["Health"][0] = min(character["Health"][0] + 3, character["Health"][1])
            print("Your health passively replenish by 3")

        else:
            break

    if not is_alive(character):
        print("You died Lmao")
        return
    else:
        after_fight(character, monster)


# Monsters Turn
def monster_attack(character, monster):
    critical = randint(1, 10)
    critical_range = [1, 3, 7]
    if critical not in critical_range:
        character["Health"][0] -= monster["Attack"][0]
        print(f"The monster attack you for {monster['Attack'][0]} leaving you with {character['Health'][0]} health \n")

    else:
        character["Health"][0] -= monster["Attack"][1]
        print("The monster caught hit you in a vulnerable spot!")
        print(f"The monster attack you for {monster['Attack'][1]} leaving you with {character['Health'][0]} health \n")
    return


# Prints Users Usable Skills
def print_user_skills(user):
    index = 1
    max_skill_name_length = max(len(skill[0]) for skill in user["Skill"].values())
    print(chr(0x2550) * 60)

    for skill in user["Skill"].values():
        skill_name = skill[0]
        damage = skill[1]
        mana_cost = skill[2]

        # Adjust the padding for the "Damage" value based on the maximum skill name length
        spacing = max_skill_name_length - len(skill_name) + 1

        print(f" {Fore.LIGHTYELLOW_EX}{index} Skill: {skill_name}{Fore.RESET}"
              f"{' ' * spacing}Damage: {Fore.LIGHTRED_EX}{damage}{Fore.RESET}"
              f" \tMana Cost: {Fore.LIGHTCYAN_EX}{mana_cost}")
        index += 1

    print(chr(0x2550) * 60)


def fight_with_skill(character, monster):
    print_user_skills(character)

    while True:
        user_choose_skill = int(input("What skill do you want to use:\n"))

        if user_choose_skill not in list(character['Skill'].keys()):
            print_user_skills(character)
        else:
            break

    chosen_skill_name = character["Skill"][user_choose_skill][0]
    chosen_skill_damage = character["Skill"][user_choose_skill][1]
    chosen_skill_mana_cost = character["Skill"][user_choose_skill][2]

    if character["Mana"][0] < chosen_skill_mana_cost:
        print(f"{Fore.LIGHTRED_EX}You need more Mana to cast {chosen_skill_name}")
        print()
        return
    else:
        character["Mana"][0] -= chosen_skill_mana_cost
        print(f"You started casting {Fore.LIGHTCYAN_EX}{chosen_skill_name}")
        monster["Health"] -= chosen_skill_damage

    if monster["Health"] <= 0:
        return
    else:
        print(f"{Fore.LIGHTCYAN_EX}{chosen_skill_name} hit the monster for {chosen_skill_damage} "
              f"leaving its Health {Fore.LIGHTRED_EX}{monster['Health']}")
        print()
        monster_attack(character, monster)
        return


def main():
    pass


if __name__ == "__main__":
    main()
