def main():
    #error = False
    div_num_s = 0

    line = input("Enter the starting point of the range:\n")
    sp = int(line)

    line = input("Enter the end point of the range:\n")
    ep = int(line)

    #line = input("Enter the divisor by which the numbers must be divisible:\n")
    # div = int(line)
    while True:
        line = input("Enter the divisor by which the numbers must be divisible:\n")
        div = int(line)
        if div <= 0:
            print("The divisor must be positive!")
        else:
            break

    for i in range(sp, ep + 1):
        if i % div == 0:
            div_num_s = div_num_s + i
            print("+{:6d}".format(i))
    print("={:6d}".format(div_num_s))
main()