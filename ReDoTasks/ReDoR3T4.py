def main():
    print("Welcome to play Nim with 2 players!")

    line = input("How many sticks are there at the start?\n")
    n_stk = int(line)

    if n_stk <= 0:
        print("error message***")

    line = input("Maximum sticks per turn?\n")
    n_max_stk = int(line)

    if n_max_stk <= 0:
        print("error message")

    p1 = "It is Player 1's turn"
    p2 = "It is Player 2's turn"
    player = p1
    n_stk_left = n_stk
    min = 1
    # max = n_max_stk

    while n_stk_left > n_max_stk:
        print()
        print(f"There are {n_stk_left} sticks left.")
        print(f"{player}")
        print(f"How many sticks to take ({min}...{n_max_stk}?)")
        line = input()
        pick_stk = int(line)

        while pick_stk <= 0 or pick_stk > n_max_stk:
            print(f"You must take between {min} and {n_max_stk} sticks! Try again!")
            print(f"How many sticks to take ({min}...{n_max_stk}?)")
            line = input()
            pick_stk = int(line)

        n_stk_left += -pick_stk

        if player == p1:
            player = p2

        else:
            player = p1

    print()
    print(f"There are {n_stk_left} sticks left.")
    print(f"{player}")
    print(f"How many sticks to take ({min}...{n_stk_left})")
    line = input()
    pick_stk = int(line)

    while pick_stk != n_stk_left:
        print(f"You must take between {min} and {n_max_stk} sticks! Try again!")
        print(f"How many sticks to take ({min}...{n_stk_left})")
        line = input()
        pick_stk = int(line)

    n_stk_left += -pick_stk

    print(f"There are {n_stk_left} sticks left.\n"
          f"{player} won!")


main()