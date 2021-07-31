# # #
# # # #
# # # # line = ''   #input("enter")
# # # #
# # # # if not line:
# # # #     print("not character")
# # # #
# # # # #if line == ''
# # #
# # # list_of_strings = ["violet", "beard moss", "rowan"]
# # #
# # # sorted_l = sorted(list_of_strings)
# # #
# # # for i in range(len(sorted_l)):
# # #     print(sorted_l[i])
# # #
# # # # for e in list_of_strings:
# # # #     print(e)
# # #
# #
# # # # a = ["pal", ["sal", '9ners'], "elcy"]
# # # #
# # # # for e in a:
# # # #     for e2 in e:
# # # #         print(e2)
# #
# #
# # def print_in_alphabetical_order(list_of_strings):
# #
# #     sorted_list = sorted(list_of_strings)
# #     for e in sorted_list:
# #         print(e)
# #
# # print_in_alphabetical_order(['aaa', 'aaa', 'bbb', 'ccc', 'ccc', 'ccc'])
#
#
#
# def average_student_class_size(c):
#     s_n_of_student_in_each_classes = []
#     for e in c:
#         n_of_student_in_each_classes = e ** 2  # number of student in each class size
#         s_n_of_student_in_each_classes.append(n_of_student_in_each_classes)  # storing number of student in each class size
#
#     num = sum(s_n_of_student_in_each_classes)
#     denom = sum(c)
#     frac = num / denom
#     return frac
#
#
# a = average_student_class_size([30, 10, 40, 20, 50])
# print()
#
# def filter_sizes(list_of_ints, lower_limit):
#     filtered_list = []
#     for i in list_of_ints:
#         if i >= lower_limit:
#             filtered_list.append(i)
#
#     return filtered_list

#     avg_f_lit = sum(filtered_list) / len(filtered_list)
#     print(avg_f_lit)
#     print(filtered_list)
#
# r_flt_size = filter_sizes([30, 10, 40, 20, 50], 40)
#
# print(r_flt_size)


# def roll(die):
#     DICES = die
#     if DICES == 0:
#         return RED[:]
#
#     elif DICES == 1:
#         return BLUE[:]
#
#     else:
#         return OLIVE[:]
#
# # for element in my_list:
#
# # for index in range(some_integer):
# # for index in range(len(my_list)):
