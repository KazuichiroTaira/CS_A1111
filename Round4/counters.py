def count_up():
    line = input("Up to which number should I count?\n")
    print()
    ncu = int(line)
    for i in range(1, ncu + 1, 1):
        print(i)


def count_down():
    line = input("From which number should I count down?\n")
    print()
    ncd = int(line)
    for i in range(ncd, -1, -1):
        print(i)


def main():
    print("This program counts numbers")
    choice = input("Count 'up' or 'down':\n")

    if choice == 'up':
        count_up()

    elif choice == 'down':
        count_down()

    else:
        print("Unknown choice. The program ends")


main()
