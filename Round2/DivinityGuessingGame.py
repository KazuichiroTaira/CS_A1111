def main():
    hide_num = [3, 5, 8, 11]
    print("Try to guess a number which is divisible by exactly 2 of the hidden numbers!")
    nog = 0  # number of guess
    zeros = 99999
    while zeros != 2:
        line = input("Enter a guess:\n")
        line = line.replace(",", "")
        guess = int(line)
        nog = nog + 1
        r0 = guess % hide_num[0]
        r1 = guess % hide_num[1]
        r2 = guess % hide_num[2]
        r3 = guess % hide_num[3]
        rs = [r0, r1, r2, r3]
        zeros = rs.count(0)
        print("Your number was divisible by", zeros, "of the numbers.")
        if zeros == 2:
            print("Congratulations, you figured out a valid number!")
            print("It took you", nog, "guesses.\nThe hidden divisors were " + str(hide_num[0]) + ', '
                  + str(hide_num[1]) + ', ' + str(hide_num[2]) + ' and ' + str(hide_num[3]) + ".")
        else:
            print("Try again!")
main()