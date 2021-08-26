def change(number, numbers):
    # print(number, numbers)

    number = 5
    numbers[0] = numbers[1] - numbers[2]
    # print(numbers)    # Numbers[0] become 2 (8-6, as num[1] - num[2]), where used to be 10
    # print(number)
    return number
    return numbers


def main():

    list1 = [10, 8, 6]
    print(list1, "before function 'change'")

    Chiffre = 1
    change(Chiffre, list1)

    print(list1, "after the function")

    print(Chiffre, "original")
    for item in list1:
        print(item, "original")


main()