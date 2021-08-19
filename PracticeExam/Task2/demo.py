def mystery1(speed):
    print("Your speed was", speed, "km/h.")
    if speed >= 67:
        print("Oh no, better prepare yourself for a fine.")
    elif speed < 0:
        print("Negative speed is not possible.")
    else:
        print("You should be all good.")


def mystery2(list1, number):
    i = 0

    while i < len(list1):
        v = list1[i]
        i += 1
        if v % number != 0:
            return False

    return True


def mystery3(string1, string2):
    result = ""
    for i in range(len(string1)):
        result += string1[i] + string2[i]
    return result


def mystery4(list1, list2):
    i = 0
    result = 0
    while i < len(list1):
        v_list1 = list1[i]
        v_list2 = list2[i]
        if v_list1 > v_list2:
            result = result + v_list1

        else:
            pass

        i += 1
    return result


def main():
    print("2a)")
    mystery1(55)
    print()

    print("2b)")
    print("This should work:", mystery2([2, 4, 6, 8], 2))
    print("This should fail:", mystery2([5, 49, 10, 37, 52, 10, 4], 5))
    print()

    print("2c)")
    print("Results should be 'abcdefgh'. Your result is following:", mystery3("aceg", "bdfh"))
    print()

    print("Tehtava 2d)")
    print("Result should be 10. Your result is following:", mystery4([1, 4, 9], [0, 5, 8]))
    print()


main()
