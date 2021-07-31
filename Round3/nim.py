def main():
    print("Welcome to play Nim with 2 players!")

    line = input("How many sticks are there at the start?\n")
    stc = int(line)
    line = input("Maximum sticks per turn?\n")
    max_stc = int(line)

    lft_stc = stc
    min_stc = int(1)
    p = 1

    print(f"\nThere are {lft_stc:} sticks left.")
    print(f"It is Player {p:}'s turn")

    while lft_stc > 0:

        if lft_stc <= max_stc:
            max_value = lft_stc

        else:
            max_value = max_stc

        line = input(f"How many sticks to take ({min_stc:} ... {max_value:})?\n")
        rmv_stc = int(line)

        if rmv_stc < min_stc or rmv_stc > max_value:
            print(f"You must take between {min_stc} and {max_value} sticks! Try again!")

        else:

            lft_stc = lft_stc - rmv_stc
            print(f"\nThere are {lft_stc:} sticks left.")

            if lft_stc > 0:

                if p == 1:
                    p = 2
                else:
                    p = 1

                print(f"It is Player {p:}'s turn")

    print(f"Player {p:} won!")

main()

