"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
import battle


def check_if_boss_is_alive(character, boss):
    if 1 in character["Goal"]:
        print(f"You already defeated {boss} ")
        return False

    if 2 in character["Goal"]:
        print(f"You already defeated {boss} ")
        return False

    if 3 in character["Goal"]:
        print(f"You already defeated {boss} ")
        return False

    if 4 in character["Goal"]:
        print(f"You already defeated {boss} ")
        return False

    return True


def fight_the_boss(character, boss):
    battle.fight(character, boss)

    if boss['Health'] <= 0:
        character["Goals"].append(1)
        print("You defeated one of the 4 pillars")

    elif boss['Health'] >= 0 and character['Health'][0] > 0:
        print("You successfully run from the Pillar Boss")

    else:
        print("You died try, again next time")


def in_special_coordinates(character, board):
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 1 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 8 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 1 and board["Level"] == 1:
        return True
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 8 and board["Level"] == 1:
        return True
    return False


def which_boss(character):
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 1:
        return 1
    if character["X-coordinate"] == 1 and character["Y-coordinate"] == 8:
        return 2
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 1:
        return 3
    if character["X-coordinate"] == 8 and character["Y-coordinate"] == 8:
        return 4


def semi_boss_stage(character, board):
    if in_special_coordinates(character, board):
        if board["Level"] == 1:
            level_1_bosses = {
                1: {"Name": "North Pillar: Black Tortoise", "Health": 700, "Attack": (10, 20), "Dodge": 0,
                    "Experience": 300},
                2: {"Name": "East Pillar: Azure Dragon", "Health": 550, "Attack": (17, 34), "Dodge": 10,
                    "Experience": 300},
                3: {"Name": "West Pillar: White Tiger", "Health": 400, "Attack": (18, 36), "Dodge": 20,
                    "Experience": 300},
                4: {"Name": "South Pillar: Vermilion Bird", "Health": 500, "Attack": (20, 42), "Dodge": 10,
                    "Experience": 350}
            }
            print("You have reached one of the four pillars of this stage")

            boss = which_boss(character)

            if not check_if_boss_is_alive(character, level_1_bosses[boss]):
                return

            else:
                fight_the_boss(character, level_1_bosses[boss])

    else:
        return


def main():
    pass


if __name__ == "__main__":
    main()
