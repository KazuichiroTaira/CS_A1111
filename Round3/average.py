def main():
    error = False
    s = 5
    sum_of_crd = 0
    sum_of_crrs = 0
    line = input("Enter the number of courses. \n")
    c = int(line)
    if c <= 0:
        error = True

    else:
        for i in range(c):
            line = input("  Enter the number of credits for the next course. \n")
            crd = float(line)
            line = input("Enter the grade for this course. \n")
            grd = int(line)

            # if not (crd > 0 and grd > 0):
            if crd <= 0 or grd <= 0:
                error = True

            crrs = (crd * (grd / s))
            sum_of_crrs = sum_of_crrs + crrs
            sum_of_crd = sum_of_crd + crd

    if error:  # error is True // error == True
        print("The average cannot be calculated.")
    else:
        r = (sum_of_crrs / sum_of_crd) / 20 * 100
        print("The weighted average of the grades is {:.2f}.".format(r))
main()


# def main():
#     s = 5
#     sum_of_crd = 0
#     sum_of_crrs = 0
#     line = input("Enter the number of courses.\n")
#     c = int(line)
#     for i in range(c):
#         line = input("Enter the number of credits for the next course.\n")
#         crd = float(line)
#         line = input("Enter the grade for this course.\n")
#         grd = int(line)
#         if crd >= 0 and grd >= 0:
#             crrs = (crd * (grd / s))
#             sum_of_crrs = sum_of_crrs + crrs
#             sum_of_crd = sum_of_crd + crd
#         else:
#             print("The average cannot be calculated.")
#
#     r = (sum_of_crrs / sum_of_crd) / 20 * 100
#     print("The weighted average of the grades is {:.3}".format(r))
# main()