"""
Richard Maceda
A01378156
Richard Li
A00995183
"""
import battle


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


def achieved_goal(character, board):
    if in_special_coordinates(character, board):
        if board["Level"] == 1:
            level_1_bosses = {
                1: {"Name": "North Pillar: Black Tortoise", "Health": 700, "Attack": (10, 20), "Dodge": 0,
                    "Experience": 300},
                2: {"Name": "East Pillar: Azure Dragon", "Health": 550, "Attack": (15, 35), "Dodge": 10,
                    "Experience": 300},
                3: {"Name": "West Pillar: White Tiger", "Health": 400, "Attack": (15, 35), "Dodge": 20,
                    "Experience": 300},
                4: {"Name": "South Pillar: Vermilion Bird", "Health": 500, "Attack": (20, 30), "Dodge": 10,
                    "Experience": 300}
            }
            print("You have reached one of the four pillars of this stage")
            boss = which_boss(character)
            battle.fight(character, level_1_bosses[boss])

            if level_1_bosses[1]['Health'] <= 0:
                print("You defeated one of the 4 pillars")
            elif level_1_bosses[1]['Health'] >= 0 and character['Health'][0] > 0:
                print("You successfully run from the Pillar Boss")
            else:
                print("You died try, again next time")
    else:
        return


def main():
    pass


if __name__ == "__main__":
    main()
