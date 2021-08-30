def count_up(num):
    for i in range(1, num+1):
        print(i)


def count_down(num):
    for i in range(num, -1, -1):
        print(i)


def main():
    print("This program counts numbers.")
    choice = input("Count 'up' or 'down':\n")

    num = int(input("From which number should I count down?\n"))
    print()

    if choice == "up":
        count_up(num)

    elif choice == "down":
        count_down(num)

    else:
        print("Unknown choice. The program ends.")


main()