def main():
    error = False
    scale_of_grade = 5
    sum_of_adjusted_course_grade = 0
    sum_of_course_credits = 0

    line = input("Enter the number of courses. \n")
    number_of_courses = int(line)

    if number_of_courses <= 0:
        error = True

    else:
        for i in range(number_of_courses):
            line = input("Enter the number of credits for the next course.\n")
            a_course_credits = float(line)
            line = input("Enter the grade for this course. \n")
            a_course_grades = int(line)

            # if not (crd > 0 and grd > 0):
            if a_course_credits <= 0 or a_course_grades <= 0:
                error = True

            a_adjusted_course_grade = (a_course_credits * (a_course_grades / scale_of_grade))
            sum_of_adjusted_course_grade += a_adjusted_course_grade
            sum_of_course_credits += a_course_credits

    if error:  # error is True // error == True
        print("The average cannot be calculated.")

    else:
        r = (sum_of_adjusted_course_grade / sum_of_course_credits) / 20 * 100
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