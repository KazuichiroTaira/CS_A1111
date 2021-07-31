my_list1 = ['abd', 'dejgif']
my_list2 = [1.0, 2, 23, 1500]
my_list = my_list1 + my_list2

# for loop =>
# 1st method
for i in range(len(my_list)):
    print(my_list[i])

print()

# 2nd method
for element in my_list:
    print(element)


empty_list = []
for element in my_list:
    empty_list.append(f'{element}')
    # print(element)
val = "-".join(empty_list)    # the list that given as argument, which should be the list of strings.


print(val)