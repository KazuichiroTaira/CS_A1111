def main():
    length = input("Enter the length of the first jump (cm).\n")
    length = float(length)
    longest_jump = length
    sol = length
    i = 1

    while length > 0:
        length = input("Enter the length of the next jump (cm).\n")
        length = float(length)
        if length > 0:
            sol = sol + length
            i = i + 1
        if length > longest_jump:
            longest_jump = length

    if longest_jump <= 0:
        print("You did not enter any results.")
    else:
        avg = sol / i
        print("The longest jump was", int(longest_jump), "cm.")
        print("The average of the jumps was", avg, "cm.")


main()