def main():
    line = input("Enter a result of the high jumper.\n")
    x = int(line)
    if x >= 228:
        print("The jumper qualifies for the final.")
    else:
        print("The jumper does not qualify.")
main()