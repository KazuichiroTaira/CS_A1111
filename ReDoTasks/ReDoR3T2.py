def main():
    error = False
    scale = 5
    sum_of_adjusted_course_grade = 0
    sum_of_c_credits = 0

    line = input("Enter the number of courses.\n")
    n_c = int(line)     # number of courses

    if n_c <= 0:
        error = True

    else:

        for i in range(n_c):
            line = input("Enter the number of credits for the next course.\n")
            c_credit = float(line)

            line = input("Enter the grade for this course\n")
            c_grade = int(line)

            if c_credit <= 0 or c_grade <= 0:
                error = True

            a_adjusted_course_grade = (c_credit * (c_grade / scale))
            sum_of_adjusted_course_grade += a_adjusted_course_grade
            sum_of_c_credits += c_credit

    if error:
        print("The average cannot be calculated.")

    else:
        result = (sum_of_adjusted_course_grade / sum_of_c_credits) / 20 * 100
        print(f"The weighted average of the grades is {result:.2f}.")


main()
