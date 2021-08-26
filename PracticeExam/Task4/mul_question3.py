def how_many():

    condition = True
    i = 1
    while condition:
        question = input("Do you want to stop (y / n)?")
        if question == "y":
            return i

        else:
            pass

            i += 1


def main():

    print("I ask you about stopping", how_many(), "times.")


main()