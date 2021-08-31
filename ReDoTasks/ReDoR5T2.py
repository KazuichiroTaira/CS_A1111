# we assume these to be mutually exclusive lists
TREES = ["spruce", "pine", "birch", "maple", "willow", "oak"]

MUSHROOMS = ["false morel", "chantarelle", "milkcap", "funnel chantarelle",
             "brittlegill", "black trumpet", "forest lamb"]

FLOWERS = ["lily", "bluebell", "violet", "daisy", "red clover", "dandelion",
           "yarrow", "anemone"]

OTHER = 0
TREE = 1
MUSHROOM = 2
FLOWER = 3


def print_in_alphabetical_order(list_species_a_z):
    list_species_a_z.sort()
    for i in list_species_a_z:
        print(i)


def classify_species(l_species):
    it_is = OTHER

    for t in TREES:
        if l_species == t:
            it_is = TREE

    for m in MUSHROOMS:
        if l_species == m:
            it_is = MUSHROOM

    for f in FLOWERS:
        if l_species == f:
            it_is = FLOWER

    # print(f"{l_species}, {it_is}")

    return it_is


def print_content_and_summary(list_of_strings, header):

    if len(list_of_strings) == 0:
        pass

    else:
        print(f"{header} ({len(list_of_strings)})")
        for i in list_of_strings:
            print(f"  {i}")


def main():
    print("Enter the species of the items you found in the forest. Stop with empty line.")
    list_species = []
    list_species_a_z = []

    while True:
        line = str(input())

        if line == "":
            break

        list_species.append(line)
        list_species_a_z.append(line)

    print("Your finds in alphabetical order:")
    print_in_alphabetical_order(list_species_a_z)

    print()

    list_species_trees = []
    list_species_mushrooms = []
    list_species_flowers = []
    list_species_others = []

    for i in list_species:

        r = classify_species(i)

        if r == 1:
            list_species_trees.append(i)

        elif r == 2:
            list_species_mushrooms.append(i)

        elif r == 3:
            list_species_flowers.append(i)

        else:
            list_species_others.append(i)

    print("You found:")
    print_content_and_summary(list_species_trees, "Trees")
    print_content_and_summary(list_species_mushrooms, "Mushrooms")
    print_content_and_summary(list_species_flowers, "Flowers")
    print_content_and_summary(list_species_others, "Others")


main()