def average_student_class_size(class_sizes):
    if len(class_sizes) == 0:
        return

    list_e_squared = []
    for e in class_sizes:
        e_squared = e ** 2
        list_e_squared.append(e_squared)

    num = sum(list_e_squared)
    denom = sum(class_sizes)
    frac = num / denom
    return frac


def filter_sizes(list_of_ints, lower_limit):
    filtered_list = []
    for i in list_of_ints:
        if i >= lower_limit:
            filtered_list.append(i)

    return filtered_list


def main():
    soc = []
    line = input("How many classes are there in the school:\n ")  # the sizes of classes in the school
    n_c = int(line)  # number of classes
    print("Enter the sizes of classes in the school:")
    for i in range(n_c):
        line = input("")
        soc.append(int(line))

    sorted_soc = sorted(soc)

    print("\nThe class sizes in order:")
    to_print = ''
    for e in sorted_soc:
        to_print += f'{e} '

    print(to_print[:-1])

    a = average_student_class_size(soc)
    print(f'\nThe average student is in a class of about the size {a:.0f}.\n')

    line = input("Enter a lower limit for the class sizes to examine:\n")
    lower_limit = int(line)

    print(f'Considering only the classes with at least {lower_limit:.0f} students,')

    r_flt_size = filter_sizes(soc, lower_limit)

    second_avg_std = average_student_class_size(r_flt_size)

    if second_avg_std is None:
        print(f'it is not possible to calculate the average class size (no classes). ')

    else:
        print(f"the average student is in a class of about the size {second_avg_std:.0f}.")


main()
