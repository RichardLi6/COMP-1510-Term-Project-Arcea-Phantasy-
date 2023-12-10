"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
# Builtin Modules
import random
from random import randint


# Non Builtin Modules
import colorama
from colorama import Fore
colorama.init(autoreset=True)


# Checks whether the character is alive
def is_alive(character):
    """
    function checks if user is alive

    :param character: a dictionary representing that character's stats
    :post-condition: checks the character Health Value
    :return: return False if character Health is equal to or less than zero
    :return: return True if character Health is greater than 0
    """
    if character["Health"][0] <= 0:
        return False

    else:
        return True


# Heal option for User
def heal_character(character):
    """
    function regenerates characters health and mana

    :param character: a dictionary of the character
    :pre-condition: character must be a dictionary containing the user's character values
    :pre-condition: character Mana key has value greater than 0
    :pre-condition: character Health key has value greater than 0
    :post-condition: regenerate the user mana base on mana scaling
    :post-condition: regenerate the user health base on health scaling
    """
    heal_scaling = {1: 11, 2: 15, 3: 17, 4: 20, 5: 23, 6: 28}
    mana_scaling = {1: 13, 2: 17, 3: 21, 4: 25, 5: 28, 6: 35}

    character_level = character["Level"]
    health_generated = heal_scaling[character_level]
    mana_generated = mana_scaling[character_level]

    print("You took a quick sidestep to regenerate yourself")
    print(f"You regenerated {Fore.LIGHTGREEN_EX}{health_generated} Health")
    print(f"You regenerated {Fore.LIGHTCYAN_EX}{mana_generated} Mana")
    character["Health"][0] = min(character["Health"][0] + health_generated, character["Health"][1])
    character["Mana"][0] = min(character["Mana"][0] + mana_generated, character["Mana"][1])


# Function that generates a monster
def generate_monster():
    """
    function generates a monster

    :post-condition: generate a random monster during a random encounter
    :return: return a dictionary containing the monster's stats
    """
    beginner_monsters_list = {
        1: {"Name": "Slime", "Health": 60, "Attack": (7, 10), "Experience": 15},
        2: {"Name": "Undead", "Health": 80, "Attack": (5, 7), "Experience": 15},
        3: {"Name": "Imp", "Health": 50, "Attack": (9, 15), "Experience": 20},
        4: {"Name": "Golem", "Health": 120, "Attack": (6, 8), "Experience": 27},
        5: {"Name": "Fallen", "Health": 20, "Attack": (12, 15), "Experience": 10},
        6: {"Name": "Cthulhu", "Health": 50, "Attack": (10, 10), "Experience": 15}
    }

    random_number = randint(1, 6)
    monster = beginner_monsters_list[random_number]
    return monster


# Prints the introduction whenever fighting
def fight_introduction(character, monster):
    """
    function prints battle stats of character and monster

    :param character: a dictionary of the character
    :param monster: a dictionary of the monster
    :precondition: character must be a dictionary containing the user's character values
    :precondition: monster must be a dictionary containing the monster's stats
    :post-condition: prints the users health and mana
    :post-condition: prints the monster's health
    """
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
    """
    function prints the after effects winning a fight

    :param character: a dictionary of the character
    :param monster: a dictionary of the monster
    :precondition: character must be a dictionary containing the user's character values
    :precondition: monster must be a dictionary containing the monster's stats
    :post-condition: inform the user winning against the monster and its rewards
    :post-condition: regenerate both mana and health  of the character
    """
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


# Passive Regeneration of Character during fights
def passive_regeneration(character):
    """
    function regenerates characters health and mana slightly

    :param character: a dictionary of the character
    :precondition: character must be a dictionary containing the user's character values
    :post-condition: regenerates the character's health and mana during fights
    """
    character["Mana"][0] = min(character["Mana"][0] + 5, character["Mana"][1])
    print("Your mana passively replenish by 5")

    character["Health"][0] = min(character["Health"][0] + 4, character["Health"][1])
    print("Your health passively replenish by 3")


# Print How much you damage the monster
def normal_attack_description(character, monster):
    """
    function prints description of character normal attack damage

    :param character: a dictionary of the character
    :param monster: a dictionary of the monster
    :precondition: character must be a dictionary containing the user's character values
    :precondition: monster must be a dictionary containing the monster's stats
    :post-condition: prints how much the user's character damage the monster
    """
    print(f"You slashed the monster for {Fore.WHITE}{character['Attack']}{Fore.RESET} leaving its Health "
          f"{Fore.LIGHTRED_EX}{monster['Health']}")
    print()


# Prompts user for choice when in fight
def user_prompt():
    """
    function prompts user action when in fight

    :post-condition: ask user what they want to do whenever they encounter a monster
    :return: a number in string format corresponding to user's choice
    """
    user_input = input(f"\n{chr(0x2554)}{chr(0x2550) * 27}{chr(0x2557)}\n"
                       f"{chr(0x2551)}  What do you want to do:  {chr(0x2551)}\n"
                       f"{chr(0x2551)}                           {chr(0x2551)}\n"
                       f"{chr(0x2551)}    1 = Normal Attack      {chr(0x2551)}\n"
                       f"{chr(0x2551)}    {Fore.LIGHTMAGENTA_EX}2 = Skill Attack{Fore.RESET}       {chr(0x2551)}\n"
                       f"{chr(0x2551)}    {Fore.LIGHTGREEN_EX}3 = Heal{Fore.RESET}               {chr(0x2551)}\n"
                       f"{chr(0x2551)}    {Fore.LIGHTYELLOW_EX}4 = Flee{Fore.RESET}               {chr(0x2551)}\n"
                       f"{chr(0x255A)}{chr(0x2550) * 27}{chr(0x255D)}\n"
                       "Type a number to corresponding action: \n")
    return user_input


# Function whenever Character is in a fight
def fight(character, monster):
    """
    function runs the fight of character and monster

    :param character: a dictionary of the character
    :param monster: a dictionary of the monster
    :precondition: character must be a dictionary containing the user's character values
    :precondition: monster must be a dictionary containing the monster's stats
    :post-condition: runs the sequence of command involve during the character fighting the monster
    :post-condition: function ends when character dies or monster dies
    """
    user_choices = ("1", "2", "3", "4")

    while character["Health"][0] >= 0 and monster["Health"] > 0:

        fight_introduction(character, monster)
        user_input = user_prompt()

        if user_input not in user_choices:
            print("Please choose a number from the choices given")
            continue

        if user_input == "4":
            if try_to_flee_successfully(character):
                print(f"You run without ever looking back")
            return

        elif user_input == "1":
            monster["Health"] -= character["Attack"]

            if monster["Health"] <= 0:
                break

            else:
                normal_attack_description(character, monster)
                monster_attack(character, monster)

        elif user_input == "3":
            heal_character(character)
            monster_attack(character, monster)

        else:
            fight_with_skill(character, monster)
            monster_attack(character, monster)

        if is_alive(character):
            passive_regeneration(character)

        else:
            break

    if not is_alive(character):
        print("You died\nGAME OVER")
        return

    else:
        after_fight(character, monster)


# Monsters Turn
def monster_attack(character, monster):
    """
    function runs the monster's turn again character in fights

    :param character: a dictionary of the character
    :param monster: a dictionary of the monster
    :precondition: character must be a dictionary containing the user's character values
    :precondition: monster must be a dictionary containing the monster's stats
    :post-condition: subtracts the character's health base in monster attack
    :post-condition: if a critical hit occurs subtracts the character's health base on monster's critical attack
    """

    critical = randint(1, 10)
    critical_range = [1, 3, 7]
    if critical not in critical_range:
        print(f"The monster attack you for {monster['Attack'][0]} leaving you with {character['Health'][0]} health \n")
        character["Health"][0] -= monster["Attack"][0]

    else:
        print("The monster caught hit you in a vulnerable spot!")
        print(f"The monster attack you for {monster['Attack'][1]} leaving you with {character['Health'][0]} health \n")
        character["Health"][0] -= monster["Attack"][1]


# Prints Users Usable Skills
def print_user_skills(user):
    """
    function prints user's available to use skills

    :param user: a dictionary of the character
    :precondition: user must be a dictionary containing the user's character values
    :post-condition: prints the user's character available skills for use
    """
    index = 1
    max_skill_name_length = max(len(skill[0]) for skill in user["Skill"].values())
    print(chr(0x2550) * 60)

    for skill in user["Skill"].values():
        skill_name = skill[0]
        damage = skill[1]
        mana_cost = skill[2]

        # Adjust the padding for the "Damage" value based on the maximum skill name length
        spacing = max_skill_name_length - len(skill_name) + 1

        print(f" {Fore.LIGHTYELLOW_EX}{index}{Fore.RESET} Skill: {Fore.LIGHTMAGENTA_EX}{skill_name}{Fore.RESET}"
              f"{' ' * spacing}Damage: {Fore.LIGHTRED_EX}{damage}{Fore.RESET}"
              f" \tMana Cost: {Fore.LIGHTCYAN_EX}{mana_cost}")
        index += 1

    print(chr(0x2550) * 60)


def fight_with_skill(character, monster):
    """
    function runs the commands when character pick skill attack option from user prompt

    :param character: a dictionary of the character
    :param monster: a dictionary of the monster
    :precondition: character must be a dictionary containing the user's character values
    :precondition: monster must be a dictionary containing the monster's stats
    :post-condition: Character will use consume mana base on the skill being use
    :post-condition: Monster will take damage base on the attack of the skill being used
    :return: None
    """
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
        print(f"You started casting {Fore.LIGHTMAGENTA_EX}{chosen_skill_name}")
        monster["Health"] -= chosen_skill_damage

    if monster["Health"] <= 0:
        return
    else:
        print(f"{Fore.LIGHTCYAN_EX}{chosen_skill_name} hit the monster for {chosen_skill_damage} "
              f"leaving its Health {Fore.LIGHTRED_EX}{monster['Health']}")
        print()
        return


def try_to_flee_successfully(character):
    """
    function when user is trying to flee in the final boss stage

    :param character: a dictionary of the character
    :precondition: character must be a dictionary containing the user's character values
    :post-condition: character will be able to run from the final boss at 70% chance
    :return: return Boolean True if character escaped successfully otherwise Boolean False
    """
    chance = randint(1, 10)
    cannot_flee_chance = (1, 5, 10)

    if chance not in cannot_flee_chance:
        print(f"You look back and started running")
        return False
    else:
        print("You tried to flee but you were bluntly hit and failed to escape")
        print(f"You took {Fore.LIGHTRED_EX} 5 {Fore.RESET} damage")
        character["Health"][0] -= 5
        return True



