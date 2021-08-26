import postal_area as PAM   # Postal Area Module


def create_areas():
    code1 = input("Give the area code of the first area.\n")
    # code1 = 65100
    people1 = int(input("Give the number of people living in this area.\n"))
    # people1 = 5389

    code2 = input("Give the area code of the second area.\n")
    # code2 = 54800
    people2 = int(input("Give the number of people living in this area.\n"))
    # people2 = 305

    """"
    Task1
    Create two areas with the zip codes provided above
    """

    first = PAM.PostalArea(code1, people1)     # fill this line for the first postcode
    second = PAM.PostalArea(code2, people2)    # fill this line for the first postcode

    return first, second


def add_test_results(area):
    positives = int(input("How many people have got a positive corona test result?\n"))
    negatives = int(input("How many people have got a negative corona test result?\n"))

    """"
    Task2
    Add a user to the given range of the parameter based on test results
    Enter a command below this comment.
    """

    area.change_statistics(positives, negatives, 0)


def add_dead(area):
    dead = int(input("How many people have died from corona?\n"))

    """"
    Task3
    Add a user to the given range of the parameter
    - based on the information provided by the number of dead.
    Enter a command below this comment.
    """

    area.change_statistics(0, 0, dead)


def check_amount_of_sick(area):
    """
    Task4
    Call the required methods that provide area information,
    i.e. area code as well as positive test result methods
    that indicate the relative amount of recipients.
    """

    amount = area.calculate_ratio_of_sick()     # Add a method call
    area_code = area.get_code()                 # Add a method call

    amount = amount * 100

    print(f"{amount:.2f}% of people living in postal area "
          f"{area_code:s} have got a positive corona test result.")


def which_has_higher_ratio(first_area, second_area):
    """
    Fill in the conditional statement of the selection box
    with two range objects call to a comparative method.
    Also complete the method call to find out the area code.

    Note: the two given paramater in this function is
    - area code:65100, people:5389, positive:32, negative:2542, dead: 3
    - area code:54800, people:305, positive:3, negative:97, dead: 0

    ########         Original Example code          #############

    area = None
    if "": # type the correct command anywhere
        area = first_area
    else:
        area = second_area

    area_code = "" # enter any command asking for the area code
    print ("Area {: s} has relatively more people that have a corona infection.". format (area_code))

    ############################################################
    """

    compare = first_area.compare_areas(second_area)

    area = None

    if compare is False:
        area = second_area
    else:  # type the correct command
        area = first_area

    area_code = area.get_code()  # type the command asking for the area code

    print(f"Area {area_code:s} has relatively more people that have a corona infection.")


def print_areas(first, second):
    """
    Print the data of the regions using their __str __ method correctly.

    Note: I guess I should not call it directly...
    print(PAM.PostalArea.__str__(first))  ---> x
    print(PAM.PostalArea.__str__(second)) ---> x
    """

    first_area = first.PAM.PoatalArea.__str__()
    second_area = second.__str__()

    print("Area information:")
    print(first_area)
    print(second_area)


def main():
    """
    No need to modify below!!!
    """
    first_area, second_area = create_areas()

    print("******* At the beginning")
    print_areas(first_area, second_area)
    print()

    print("Add test results to the areas.")
    print("For the first area:")
    add_test_results(first_area)
    print("For the second area:")
    add_test_results(second_area)

    print("Add dead.")
    print("For the first area:")
    add_dead(first_area)
    print("For the second area:")
    add_dead(second_area)
    print()

    print("******** After adding the statistics")
    print_areas(first_area, second_area)
    print()

    print("Ratio of sick people:")
    check_amount_of_sick(first_area)
    check_amount_of_sick(second_area)
    print()

    print("Which area has more sick people?")
    which_has_higher_ratio(first_area, second_area)
    print()

    print("****** At the end:")
    print_areas(first_area, second_area)


main()
