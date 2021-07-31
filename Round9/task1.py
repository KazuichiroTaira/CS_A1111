# Y1 SUMMER 2021
# Basic Course in Programming Y1
# Author Kerttu Pollari-Malmi
# A test program for class Student.

import student


def read_int():
    ok = False
    luku = None
    while not ok:
        try:
            luku = int(input())
            ok = True
        except ValueError:
            print("ERROR: You did not enter a valid integer!")
            print("Try again!")
    return luku


def main():
    s = student.Student("xxx", "xxx")
    for i, (exam, assigment, expected) in enumerate((
            (2, 0, 0), (0, 5, 0),
            (2, 4, 2), (4, 5, 5),
            (3, 0, 1), (3, 2, 2))):
        s.change_examgrade(exam)
        s.change_assignmentgrade(assigment)
        print("student", i)
        print("computed", s.calculate_finalgrade())
        print("expected", expected)
        print()
    # name1 = input("Enter the name of the first student:\n")
    # student_id1 = input("Enter the student id:\n")
    # student1 = student.Student(name1, student_id1)
    # name2 = input("Enter the name of the second student:\n")
    # student_id2 = input("Enter the student id:\n")
    # student2 = student.Student(name2, student_id2)
    #
    # print("Enter the exam grade of the first student.")
    # exam1 = read_int()
    # student1.change_examgrade(exam1)
    # print("Enter the assignment grade of the first student.")
    # exercise1 = read_int()
    # student1.change_assignmentgrade(exercise1)
    #
    # print("Enter the exam grade of the second student.")
    # exam2 = read_int()
    # student2.change_examgrade(exam2)
    # print("Enter the assignment grade of the first student.")
    # exercise2 = read_int()
    # student2.change_assignmentgrade(exercise2)
    #
    # print("Student 1:")
    # print(student1)
    # print("Course grade:", student1.calculate_finalgrade())
    #
    # print("Student 2:")
    # print(student2)
    # print("Course grade:", student2.calculate_finalgrade())
    #
    # print("Enter the new exam grade of the second student.")
    # exam2 = read_int()
    # student2.raise_examgrade(exam2)
    #
    # print("Student 2 again:")
    # print(student2)
    # print("Course grade:", student2.calculate_finalgrade())


main()