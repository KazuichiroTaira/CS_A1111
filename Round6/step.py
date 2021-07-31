def enter_values(dictionary, name, step_input):
    # Implement your code here
    str_step_list = step_input.split(",")
    step_list = []
    for e in str_step_list:
        step_list.append(int(e))

    if name in dictionary:
        dictionary[name] += step_list
    else:
        dictionary[name] = step_list


def search_by_name(dictionary, name):
    # Implement your code here
    if name in dictionary:

        steps_list = dictionary[name]
        total_steps = sum(steps_list)

    else:
        steps_list = []
        total_steps = -1

    return steps_list, total_steps


def main():
    dictionary = {}

    name = input("Enter the name of the person. Stop with an empty line.\n")
    while name != "":
        step_input = input("Enter the different day's steps on one line.\n")
        enter_values(dictionary, name, step_input)
        name = input("Enter the name of the person. Stop with an empty line.\n")

    name = input("Enter name to search. Stop with an empty line.\n")
    while name != "":

        step_list, total_steps = search_by_name(dictionary, name)

        if total_steps == -1:
            print("No information on that person.")

        else:
            print(f"{name} 's steps in a list: {step_list}")
            print(f"{name} 's total steps: {total_steps}")

        name = input("Enter name to search. Stop with an empty line. \n")

    print("Program ends.")


main()