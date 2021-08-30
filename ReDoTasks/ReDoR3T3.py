def main():
    line = input("Enter the starting point of the range:\n")
    starting = int(line)
    # starting = int(90)

    line = input("Enter the end point of the range:\n")
    ending = int(line)
    # ending = int(1200)

    line = input("Enter the divisor by which the numbers must be divisible:\n")
    divisible = int(line)

    divisors = []
    while divisible <= 0:
        print("The divisor must be positive!")
        line = input("Enter the divisor by which the numbers must be divisible:\n")
        divisible = int(line)

    for i in range(starting, ending + 1):

        if i % divisible == 0:
            divisors.append(i)
            print(f"+ {i}")

    sum_of_divisors = sum(divisors)
    print(f"= {sum_of_divisors}")


main()