# Y1 AUTUMN 2020
# Basic Course in Programming Y1
# Author: Anni Niskanen
# Template for Exercise 9.2


from golfer import Golfer
from golf_course import GolfCourse


def ask_list_of_integers():
    """
    Asks the user for integers separated by commas. Converts the inputted string into a list of integers and
    returns it.
    """
    string = input()
    list_in_characters = string.split(",")  # creates a list
    list_in_integers = []
    for character in list_in_characters:
        list_in_integers.append(int(character))
    return list_in_integers


def main():
    input("Press enter to continue.\n")

    # Create two golfers and one golf course here
    p1_name = input("Name of the first golfer:\n")
    p2_name = input("Name of the second golfer:\n")
    g_name = input("Name of the golf course:\n")
    print("Par scores of the golf course (separated by commas):")
    scores = ask_list_of_integers()
    slope = int(input("Slope rating of the golf course:\n"))
    input()
    print("The golfers:")
    p1 = Golfer(p1_name)
    p2 = Golfer(p2_name)
    g = GolfCourse(g_name, scores, slope)
    # Print information about the golfers and the golf course here
    for p in p1, p2:
        print(p)

    print("\nThe golf course:")
    print(g)
    input()

    # The golfers play a round of Golf here
    print(
        f"{p1.get_name()} and {p2.get_name()} are off to play a round of Golf in {g.get_name()}!")
    print(f"\nEnter {p1.get_name()}'s results (separated by commas):")
    r_p1 = ask_list_of_integers()

    print(f"Enter {p2.get_name()}'s results (separated by commas):")
    r_p2 = ask_list_of_integers()
    input()

    # Print the results of the first golfer here
    s_p1 = p1.get_round_statistics(g, r_p1)
    print(f"{p1.get_name()}'s round looks like this:")
    print(s_p1)
    input()

    # Print the results of the second golfer here
    s_p2 = p2.get_round_statistics(g, r_p2)
    print(f"And {p2.get_name()}'s round looks like this:")
    print(s_p2)
    input()

    # Determine and print which golfer won the game here
    p1_wins = p1.compare_scores(r_p1, r_p2)
    if p1_wins:
        winner = p1.get_name()
    else:
        winner = p2.get_name()
    print(f"{winner} won the round!")
    input()

    # Print how much the golfers' handicaps lowered here
    print(f"The golfers have played {g.get_amount_of_holes()} holes in {g.get_name()} and count their new handicaps.")
    h_p1 = p1.play_round(g, r_p1)
    h_p2 = p2.play_round(g, r_p2)
    print(f"{p1.get_name()}'s handicap lowered by {h_p1}.")
    print(f"{p2.get_name()}'s handicap lowered by {h_p2}.")
    input()

    # Print information about the golfers again here
    print("The golfers again:")
    for p in p1, p2:
        print(p)
    input()

    # Compare the golfers with each other and print which one has a lower handicap
    if p1.get_handicap() < p2.get_handicap():
        lower_h = p1.get_name()
    else:
        lower_h = p2.get_name()

    print(f"{lower_h} has a lower handicap.")

main()
