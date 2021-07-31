# # Division of the program into functions and the main program
# # def main():
# #     line = input("enter the temperature in degrees Fahrenheit: ")
# #     Fahrenheit = float (line)
# #     celsius = (Fahrenheit - 32) * 5.0 / 9.0
# #     print(Fahrenheit, "F on", celsius, "C")
# # main()
#
#
# # Room area
# # def main():
# #     line = input("enter room width in meters. \ n ")
# #     width = float(line)
# #     line = input("enter room length in meters. \ n ")
# #     length = float(line)
# #     area = width * length
# #     print("Room area is", area, "square meters")
# # main()
#
# #The price of the call
#
# # def potc():
# #     print("The program calculates the price of the mobile call.")
# #     line = input("Enter the call initiation fee. \ n ")
# #     initiation_fee = float(line)
# #     line = input("Enter the minute price of the call. \ n ")
# #     price_per_minute = float(line)
# #     line = input("Enter the dulation of the call in minutes. \ n ")
# #     duration = float(line)
# #     price = initiation_fee + duration * price_per_minute
# #     print("call cost is", price, "euros")
# #
# # potc()
#
# # def tcv_to_sec():
# #     print("This program changes the length of a given time period to seconds.")
# #     line = input("Enter the hours of the time period. \ n ")
# #     hours = int(line)
# #     line = input("Enter the minutes of the time period. \ n")
# #     minutes = int(line)
# #     line = input("Enter the seconds of the time period. \ n ")
# #     seconds = int(line)
# #     time_seconds = hours * 3600 + minutes * 60 + seconds
# #     print("Time period length is", time_seconds, "seconds.")
# # tcv_to_sec()
#
# def tcv_to_HMS():
#     line = input("Enter the length of the time period in seconds. \ n ")
#     length_seconds = int(line)
#     hours = length_seconds // 3600
#     sequence_seconds = length_seconds % 3600
#     minutes = sequence_seconds //60
#     seconds = sequence_seconds % 60
#     print("Length is", hours, "h", minutes, "m", seconds, "s.")
# tcv_to_HMS()
#
# def age():
#     line = input("Tell your age \n")
#     age = int(line)
#     if age < 18:
#         price = 3
#     else:
#         price = 10
#     print("Ticket price is", price, "euros")
# age()

# def ibm():
#     line = input("Enter your weight in kilograms. \n")
#     weight = float(line)
#     line = input("Enter your height in meters. \n")
#     height = float(line)
#     if height > 0.0 and height < 3.0:
#         bmi = weight / ((height)**2)
#         print("Your body mass index is", round(bmi,4))
#     else:
#         print("Invalid height - weight index cannot be calculated")
# ibm()

# The condition used can be any expression with a value of True or False
#  >	bigger than
#  <	smaller than
#  ==	equal to
#  !=	different from
#  >=	greater than or equal to
#  <=	less than or equal to

# Logical Operators
# and	and	 true if both expressions are true
# or	or	 true if at least one of the expressions is true
# not	No	 true if the following expression is false


# def ibm():
#     line = input("Enter your weight in kilograms. \n")
#     weight = float(line)
#     line = input("Enter your height in meters. \n")
#     height = float(line)
#
#     if height > 0.0 and height < 3.0:
#         bmi = weight / ((height)**2)
#         print("Your body mass index is", bmi)
#
#         if bmi < 19.0:
#             print("You are underweight")
#         if bmi >= 25.0:
#             print("You are overweight")
#
#     else:
#         print("Invalid height - weight index cannot be calculated")
# ibm()


# adding Elif to the former code
#
# def ibm():
#     line = input("Enter your weight in kilograms. \n")
#     weight = float(line)
#     line = input("Enter your height in meters. \n")
#     height = float(line)
#
#     if height > 0.0 and height < 3.0:
#         bmi = weight / ((height)**2)
#         print("Your body mass index is", bmi)
#
#         if bmi < 19.0:
#             print("You are underweight")
#         if bmi < 25.0:
#             print("Your weight is normal")
#         elif bmi < 30.0:
#             print("You are slightly over weight")
#         elif bmi < 35.0:
#             print("You are significantly over weight")
#         elif bmi < 40.0:
#             print("you are severely overweight")
#         else:
#             print ("You are morbidly overweight")
#
#     else:
#         print("Invalid height - weight index cannot be calculated")
# ibm()

# Repeat command

# def p_and_space():
#     line = input("Enter the side length of the square(cm)")
#     page = float(line)
#     while page < 0:
#         print("Page length must not be negative!")
#         line = input("Enter page length(cm)\n")
#         page = float(line)
#     area = page * page
#     print("The area of a square is", area, "cm2")
# p_and_space()

# def xitg():
#     print("Enter 10 integers, averaging them.")
#     i = 0
#     t = 0
#     while i < 10: # Here is modifiable
#         line = input("Enter the following numbers:")
#         number = int(line)
#         t = t + number
#         i = i + 1
#     avg = t / 10
#     print("Their average is", avg)
# xitg()

# Modified version - make it constant

# def avg_x_int():
#     ints = 5
#     print("Enter", ints, "integers, calculate their average.")
#     i = 0                 # initialize the revolution counter...
#     ttl = 0               # giving an initial value as 0
#     while i < ints:
#         line = input("Enter the following number: ")
#         number = int(line)
#         ttl = ttl + number
#         i = i + 1
#     avg = ttl / ints
#     print("Their average is", avg)
# avg_x_int()

# def avg_x_int():
#     print("Caluclate the average of the integers you entered.")
#     line = input("Enter the number of integers:")
#     n_ints = int(line)
#     i = 0                 # initialize the revolution counter...
#     ttl = 0               # giving an initial value as 0
#     while i < n_ints:
#         line = input("Enter the following number: ")
#         number = int(line)
#         ttl = ttl + number
#         i = i + 1
#     if n_ints > 0:
#         avg = ttl / n_ints
#         print("Their average is", avg)
#     else:
#         print("You did not enter any number.")
# avg_x_int()


# def avg_pos_num():
#     print("Computing the average of non-negative integers")
#     print("Stop the negative number")
#
#     nons = 0                                    # number of numbers
#     s = 0                                                  # sum of numbers
#     line = input("Enter the first number: ")
#     num = int(line)                                          # number
#
#     while num >= 0:
#         nons = nons + 1
#         s = s + num
#         line = input("enter the following number: ")
#         num = int(line)
#     if nons > 0:
#         avg = s / nons
#         print("Their average is ", avg)
#     else:
#         print("You did not enter any positive numbers")
# avg_pos_num()
# #
#
# def main():
#     print(". The count of the average much for non-negative integers")
#     print(". Stop the negative figure")
#     number_of_numbers = 0
#     s = 0
#     row = input('Enter the first number: ')
#     number = int(row)
#     while number >= 0:
#         number_of_numbers = number_of_numbers + 1
#         s = s + number
#         row = input("Enter the following number:")
#         number = int(row)
#     if number_of_numbers > 0:
#         average = s / number_of_numbers
#         print("Their average is", average)
#     else:
#         print("You did not enter any non-negative numbers.")
# main()


# the weather statictics
#
#
# def ntm():
#     accuracy = 0.0001
#     line = input("Which square root of a number is calculated?: ")
#     x = float(line)
#     if x < 0:
#         print("Four roots are not defined for negative numbers")
#     else:
#         guess = 1.0
#         new_guess = 0.5 * (guess + x / guess)
#         while abs(new_guess - guess) > accuracy:
#             guess = new_guess
#             new_guess = 0.5 * (guess + x / guess)
#         print("Number", x, "has square roots", new_guess)
# ntm()

# Round3 - repeat command for and range function

# def main():
#     for i in range(11): # compute x from 0 to 10
#         x = i * 6
#         print(i, "* 6 =", x)
# main()

# Or
#
# def main():
#     line = input("Enter the number of numbers. \n")
#     nom = int(line) # number of numbers
#     ttl = 0
#     print("Enter numbers one at a time.")
#     for i in range(nom):
#         line = input()
#         num = float(line) # number
#         if num > 0:
#             ttl += num
#     print("The sum of the positive numbers is", ttl)
# main()

# def main():
#     for i in range(1,11):
#         print(i, "* 6 =", i * 6)
# main()

# for i in range(5, 19, 3):
#     print(i)

# m = 5
# n = 4
# r = m * n
# print("{:3d} times {:3d} is {:6d}".format(m, n, r))

# enimi1 = "Matti"
# snimi1 = "Virtanen"
# salary1 = 2800
# enimi2 = "Tiina-Maija"
# snimi2 = "Boss"
# salary2 = 11000
#
# print("{:15s} {:15s} {:5d} euros".format(snimi1, enimi1, salary1))
# #Virtanen Matti 2800
#
# print("{:15s} {:15s} {:5d} euros".format(snimi2, enimi2, salary2))
# #Boss Tiina-Maija 11000 euros
#
#
# print("{:>15s} {:>15s} {:<5d} euros".format(snimi1, enimi1, salary1))
# #Virtanen Matti 2800 euros
#
# print("{:>15s} {:>15s} {:<5d} euros".format(snimi2, enimi2, salary2))
# # Boss Tiina-Maija 11000 euros

# page = 4.5678945
# page_area = page * page
# print("The page is {:.2f} m and a surface area {:.2f} m2".format(page, page_area))

# The site is 4.57 m and the area is 20.87 m2

# small_number = 1.2308e01
# large_number = 14.5e20
# x = small_number * large_number
# print("Multiplying {: 5.4g} and {: 8.4g} yields {: 10.4g}".format(small_number, large_number, x))

# Multiplying 12.31 and 1.45e + 21 gives 1.785e + 22

# interest_rate = 2.5
# capital = 12000
# print("You get interest {:.2f} euro".format(interest_rate / 100.0 * capital))
# #You get interest 300.00 eur

# Morgage example1
#
# def main():
#     print("The program calculates the monthly installments of the mortgage.")
#     line = input("Enter loan amount:")
#     la = float(line) #loan amount
#     line = input("Enter loan period in years:")
#     lys = int(line) #loan years
#     if lys < 1:
#         print("Too short loan period")
#     else:
#         nom = 12 * lys #numer of months
#         line = input("Enter the interest rate")
#         ir = float(line) #interest rate
#         mp = la / nom    #monthly payment
#         cap = la         #capital
#         i = 0
#         print("Total short term mortgage rate")
#         while i < nom:
#             i = i + 1
#             ird = ir / 1200.0 * cap  #interest rate diffrential
#             cap = cap - mp
#             mi = ird + mp            #monthly installment
#             print("{:2d}.{:8.2f}{:8.2f}{:8.2f}".format(i, mp, ird, mi))
# main()

#
# Morgage example2
# def main():
#     print("The program calculates the monthly installments of the mortgage.")
#     line = input("Enter loan amount:")
#     la = float(line) #loan amount
#     line = input("Enter loan period in years:")
#     lys = int(line) #loan years
#     if lys < 1:
#         print("Too short loan period")
#     else:
#         nom = 12 * lys #numer of months
#         line = input("Enter the interest rate")
#         ir = float(line) #interest rate
#         mp = la / nom    #monthly payment
#         cap = la         #capital
#         i = 0
#         print("Total short term mortgage rate:")
#         for i in range(1, nom + 1):
#             ird = ir / 1200.0 * cap  #interest rate diffrential
#             cap = cap - mp
#             mi = ird + mp            #monthly installment
#             print("{:2d}.{:8.2f}{:8.2f}{:8.2f}".format(i, mp, ird, mi))
# main()
#
# def main1A():
#     population = int(input("Enter the population of the locality\n"))
#     if population >= 500000:
#         print("Metropolis")
#     if population >= 50000:
#         print("city")
#     if population < 5000:
#         print("village")
#     else:
#         print("town")
# main1A()

#
# def main1B():
#     population = int(input("Enter the population of the locality\n"))
#     if population >= 500000:
#         print("Metropolis")
#     elif population >= 50000:
#         print("city")
#     elif population < 5000:
#         print("village")
#     elif population >= 5000:
#         print("town")
# main1B()

# def main1C():
#     population = int(input("Enter the population of the locality\n"))
#     if population >= 500000:
#         print("Metropolis")
#     if 50000 < population < 500000:
#         print("city")
#     if population < 5000:
#         print("village")
#     if 5000 < population < 50000:
#         print("town")
# main1C()


# def main2A():
#     number = int(input())
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
#     if number < 0:
#         print("Negative")
#     elif number > 0:
#         print("Positive")
#     else:
#         print("Zero")
# main2A()

# def main2B():
#     number = int(input())
#     if number % 2 == 0:
#         print("Even")
#     elif number % 2 == 1:
#         print("Odd")
#
#     elif number < 0:
#         print("Negative")
#     elif number > 0:
#         print("Positive")
#     else:
#         print("Zero")
# main2B()

# m = 11
# k = m - 4
# p = 0
# for i in range(k):
#     p = p + 1
# print(p)

# def s_f(v):
#     a = 17 - 2
#     b = a + v
#     print(v)
#     print(b)
# s_f()
#
# def main():
#     c = 100 / 2
#     print(c)
#     s_v(c)
#     print(c * 4)
#     s_f(c)
# main()
#
# def m_f():
#     b = 15
#     y = b / 3 + 1
#     print(y+b)
# m_f()
#
# def main():
#     a = 2
#     c = a * 2
#     print(a)
#     m_f()
#     print(c)
#     m_f()
# main()
#
# def pt():
#     print("  #  ")
#     print(" ### ")
#     print("#####")
# pt()
#
# def main():
#     pt()
#     pt()
#     pt()
# main()

#
#
# def  greet ():
#     name  =  input ( "Who are you?" )
#     print ( "Hello," ,  name )
#
#
# def  print_triangle ():
#     print ( "*" )
#     print ( "***" )
#     print ( "*****" )
#
#
# def  main ():
#     print ( "Start" )
#     greet ()
#     print ( "Half-choice" )
#     print_triangle ()
#     print ( "End" )
#
#
# main ()

# def c_v(c, t, r):
#     print("Investment value at the end of the year:")
#     print("year value")
#     for i in range(1, t + 1):
#         c = c * (1.0 + r / 100.0)
#         print("{:2d}.{:10.2f} euros".format(i, c))
#
# def main():
#     print("The program calculates the development of the value of the investment annually")
#     line = input("Enter the amount to be invested (EUR):")
#     t = float(line)
#     line = input("Enter the investment period (years):")
#     years = int(line)
#     line = input("Enter expected rate of return:")
#     r = float(line)
#     c_v(t, years, r)
# main()
#
#
# def s_ag_f(x_m1, y_m1, x_m2, y_m2):
#     if x_m1 * y_m2 == x_m2 * y_m1:
#         return True
#     else:
#         return False
#
# def s_ax_s(a1, b1, c1, a2, b2, c2):
#     if b1 == 0 and b2 == 0:   # straight y-axis
#         if a1 * c2 == a2 * c1:
#             return True
#         else:
#             return False
#     elif b1 * c2 == b2 * c1:
#         return True
#     else:
#         return False
#
# def s_c(a1, b1, c1, a2, b2, c2):
#     y_m = (a1 * c2 - a2 * c1) / (b1 * a2 - b2 * a1)
#     if a1 == 0:
#         x_m = (-b2 * y_m - c2) / a2
#     else:
#         x_m = (-b1 * y_m - c1) / a1
#     return x_m, y_m
#
# def ask_direction():
#     print("Enter the equation of a line")
#     a = int(input("Enter the coefficient of x:"))
#     b = int(input("Enter the coefficient of y:"))
#     c = int(input("Enter constant:"))
#     return a, b, c
#
# def main():
#     print("Search by two straight ax + by + c intersection point")
#     eka_a,  eka_b,  eka_c = ask_direction()
#     toka_a,  toka_b,  toka_c = ask_direction()
#
#     if s_ag_f(eka_a, eka_b, toka_a, toka_b) and s_ax_s(eka_a, eka_b, eka_c, toka_a, toka_b, toka_c):
#         print("Direct are the same throughout the length.")
#     elif s_ag_f(eka_a, eka_b, toka_a, toka_b):
#         print(". Direct are parallel, no intersection")
#     else:
#         x_cord, y_cord = s_c(eka_a, eka_b, eka_c, toka_a, toka_b, toka_c)
#         print("Intersection is {: .2f},{: .2f}".format(x_cord, y_cord))
# main()
# def main():
#     temp_con = []
#     temp_con.append(15.0)
#     temp_con.append(22.5)
#     temp_con.append(-12.9)
#     print(temp_con)
#     temp_con[1] = 32.0
#     print(temp_con)
#     temp_con[2] = 18
#     print(temp_con)
#     s = temp_con[1] + temp_con[2]
#     print(s)
#
#
# main()

# temp_con = []
# num = 10      # ikm = number in finnish
# i = 0
# while i < num:
#     line = float(input("Next temperature condition:\n"))
#     temp_con.append(line)
#     i += 1
#
# ttl = 0.0
# i = 0
# while i < num:
#     ttl += temp_con[i]
#     i += 1
# print(ttl)
# print(temp_con)

#
# def main():
#     temp_con = []
#     num = 5  # ikm = number in finnish
#     i = 0
#     print("Enter", num, "temperature.")
#     while i < num:
#         line = float(input("Next temperature condition:"))
#         temp_con.append(line)
#         i += 1
#
#     ttl = 0.0
#     print("Given temperature")
#     for i in temp_con:
#         print(i)
#         ttl += i
#
#     avg = ttl / num
#     print(f"average temperature{avg:.2f}")
#
#
# main()

#
# num_days_list = [2, 4, 6, 8]
# # print(type(num_days_list))
#
# num_days = 5
# temp_conditions = [0.0] * num_days
# i = 0
# while i < num_days:
#     heat = float(input("Next temperature mode:"))
#     temp_conditions[i] = heat
#     i += 1

def ask_temperature_mode():
    num = 10
    temperature = [0.0] * num
    i = 0
    print("Enter", num, "temperature mode")
    while i < num:
        celsius = float(input("Next temperature mode:"))
        temperature[i] = celsius
        i += 1
    return temperature


def print_temperature(temperature):
    print("the prescribed temperature")
    for v in temperature:
        print(v)


def calculate_average(temp_list):
    total = 0.0
    for temperature in temp_list:
        total += temperature
    num = len(temp_list)

    if num > 0:
        avg = total / num
    else:
        avg = 0.0
    return avg


def main():
    temp_list = ask_temperature_mode()
    print_temperature(temp_list)
    average = calculate_average(temp_list)
    print(f"Average temperatures is {average:.2f}")


main()
