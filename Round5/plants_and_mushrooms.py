# we assume these to be mutually exclusive lists
TREES = ["spruce", "pine", "birch", "maple", "willow", "oak"]
MUSHROOMS = ["false morel", "chantarelle", "milkcap", "funnel chantarelle", "brittlegill", "black trumpet",
             "forest lamb"]
FLOWERS = ["lily", "bluebell", "violet", "daisy", "red clover", "dandelion", "yarrow", "anemone"]

OTHER = 0
TREE = 1
MUSHROOM = 2
FLOWER = 3


def classify_species(species):
    if species in TREES:
        return TREE

    elif species in MUSHROOMS:
        return MUSHROOM

    elif species in FLOWERS:
        return FLOWER

    else:
        return OTHER


def print_in_alphabetical_order(list_of_strings):

    sorted_list = sorted(list_of_strings)
    for e in sorted_list:
        print(e)


def print_content_and_summary(list_of_strings, header):

    n = len(list_of_strings)
    if n == 0:
        return

    print(f"{header} ({n})")

    for e in list_of_strings:
        print(f"  {e}")


def main():

    user_list = []

    print("Enter the species of the items you found in the forest. Stop with empty line.")
    while True:
        line = input("")

        if line:
            user_list.append(line)

        else:
            break

    print("Your finds in alphabetical order:")
    print_in_alphabetical_order(user_list)
    print()

    trees = []
    flowers = []
    mushrooms = []
    others = []

    for e in user_list:

        c = classify_species(e)
        if c == FLOWER:
            flowers.append(e)

        elif c == MUSHROOM:
            mushrooms.append(e)

        elif c == TREE:
            trees.append(e)

        else:
            others.append(e)

    print("You found:")
    print_content_and_summary(trees, "Trees")
    print_content_and_summary(mushrooms, "Mushrooms")
    print_content_and_summary(flowers, "Flowers")
    print_content_and_summary(others, "Other")


main()
