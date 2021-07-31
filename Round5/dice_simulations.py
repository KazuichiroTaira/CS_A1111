# Y1 SUMMER 2020
# Basic Course in Programming Y1
# Author: Vilma Kahri
# Template for exercise 5.5
import random

RED = [3, 3, 3, 3, 3, 6]
BLUE = [2, 2, 2, 5, 5, 5]
OLIVE = [1, 4, 4, 4, 4, 4]
DICE_NAMES = ["Red", "Blue", "Olive"]
DICES = [RED, BLUE, OLIVE]


# The function initialises the random number generator
# with the seed number input by the user.

def init_die():
    seed_count = int(input("Give a seed for the dice.\n"))
    random.seed(seed_count)


# IMPLEMENT THE MISSING FUNCTIONS HERE
# Calls for the appropriate simulation function
# and prints the outcome of the simulation.

def roll(die):
    face_idx = random.randint(0, 5)
    dice = DICES[die]
    face_value = dice[face_idx]
    return face_value


def simulate_singles(die1, die2, rolls):

    num_v_p1 = 0
    num_v_p2 = 0
    num_draws = 0

    for i in range(rolls):
        r1 = roll(die1)
        r2 = roll(die2)

        if r1 > r2:
            num_v_p1 += 1

        elif r2 > r1:
            num_v_p2 += 1

        else:
            num_draws += 1

    return num_v_p1, num_v_p2, num_draws


def simulate_doubles(die1, die2, rolls):

    num_v_p1 = 0
    num_v_p2 = 0
    num_draws = 0

    for i in range(rolls):

        r1 = roll(die1) + roll(die1)
        r2 = roll(die2) + roll(die2)

        if r1 > r2:
            num_v_p1 += 1

        elif r2 > r1:
            num_v_p2 += 1

        else:
            num_draws += 1

    return num_v_p1, num_v_p2, num_draws


def simulate_and_print_result(die1, die2, rolls, simulation_function, header):
    wins1, wins2, draws = simulation_function(die1, die2, rolls)
    print(header)
    print("Player 1 used {:s} die and won {:d} times, so {:.1f}% of the rolls.".format(DICE_NAMES[die1], wins1,
                                                                                       wins1 / rolls * 100))
    print("Player 2 used {:s} die and won {:d} times, so {:.1f}% of the rolls.".format(DICE_NAMES[die2], wins2,
                                                                                       wins2 / rolls * 100))
    if draws != 0:
        print("{:d} draws, so {:.2f}% of the rolls.".format(draws, draws / rolls * 100))


def main():
    print("Welcome to a non-transitive dice simulation.")
    init_die()

    print("The dice:")
    for i in range(len(DICES)):
        print("{:d} for {:s}: {:}".format(i, DICE_NAMES[i], DICES[i]))

    choice1 = int(input("Choose a die for player 1:\n"))
    choice2 = int(input("Choose a die for player 2:\n"))
    rolls = int(input("How many rolls to simulate?\n"))

    simulate_and_print_result(choice1, choice2, rolls, simulate_singles, "Singles:")
    simulate_and_print_result(choice1, choice2, rolls, simulate_doubles, "Doubles:")


main()
