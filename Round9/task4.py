# Y1 SUMMER 2021
# Basic Course in Programming Y1
# A test program for Exercise 9.4

import driver as driver_module

# A helper function for reading a lap time
# Asks for input until a valid lap time in the format
# minutes:seconds:centiseconds is given.


def read_lap_time():
    lap_time_read = False
    while not lap_time_read:
        try:
            lap_time_string = input()
            parts = lap_time_string.split(":")
            minutes, seconds, centiseconds = parts
            if (len(parts) == 3) and (0 <= int(minutes) < 60) \
                                 and (0 <= int(seconds) < 60) \
                                 and (0 <= int(centiseconds) < 100):
                return lap_time_string
        except ValueError:
            pass
        print("Invalid lap time, please enter a new one:")

# A helper function for reading an integer

def read_integer():
    success = False
    while not success:
        try:
            inputted_integer = int(input())
            success = True
        except ValueError:
            print("Invalid integer, please enter a new one:")
    return inputted_integer

# Reads new Driver instances and returns them in a list.

def create_drivers(names, teams):
    print("Creating new drivers...")
    drivers = []
    for i in range(len(names)):
        new_driver = driver_module.Driver(names[i], teams[i])
        drivers.append(new_driver)
    print("There are now {:d} drivers in the competition.".format(len(drivers)))
    return drivers


# Asks for input and records a new lap time for a driver.
# A list of all Drivers is given as as list

def record_a_lap_time(drivers):
    if len(drivers) == 0:
        print("No drivers created!")
    else:
        for i in range(len(drivers)):
            print("{:d}. {:s}".format(i + 1, drivers[i].get_name()))
        print("Enter the number of a driver")
        driver_num = read_integer()
        if not (1 <= driver_num <= len(drivers)):
            print("No driver associated with that number!")
        else:
            print("Enter a lap time.")
            lap_time_string = read_lap_time()
            success = drivers[driver_num - 1].record_lap_time(lap_time_string)
            if success:
                print("The lap time was recorded.")
            else:
                print("Warning: the lap time could not be recorded.")

# Overwrites the lap time of a driver.
# A list of all Drivers is given as as list

def overwrite_lap_time(drivers):
    if len(drivers) == 0:
        print("No drivers created!")
    else:
        for i in range(len(drivers)):
            print("{:d}. {:s}".format(i + 1, drivers[i].get_name()))
        print("Enter the number of the driver whose lap time you want to overwrite.")
        driver_number = read_integer()
        if driver_number < 1 or driver_number > len(drivers):
            print("No driver associated with that number!")
        else:
            print("Enter the lap number to change.")
            lap_num = read_integer()
            print("Enter the new lap time.")
            lap_time_string = read_lap_time()
            success = drivers[driver_number - 1].overwrite_lap_time(lap_num, lap_time_string)
            if success:
                print("The lap time was overwritten.")
            else:
                print("Warning: the lap time could not be overwritten.")


# Compares two drivers.
# A list of all Drivers is given as as list

def compare_two(drivers):
    if len(drivers) == 0:
        print("No drivers created!")
    else:
        print("Comparing two drivers.\n")
        for i in range(len(drivers)):
            print("{:d}. {:s}".format(i + 1, drivers[i].get_name()))
        print("Enter the number of the 1st driver to compare.")
        driver_number1 = read_integer()
        print("Enter the number of the 2nd driver to compare.")
        driver_number2 = read_integer()
        if driver_number1 < 1 or driver_number1 > len(drivers) or \
           driver_number2 < 1 or driver_number2 > len(drivers):
            print("No driver associated with one or more of these numbers!")
        else:
            comparison_result = drivers[driver_number1 - 1].compare_best_lap_time(drivers[driver_number2 - 1])
            if comparison_result == 1:
                print("The first driver is faster.")
            elif comparison_result == -1:
                print("The second driver is faster.")
            else:
                print("The drivers are equally fast.")


# Prints out all Drivers.
# A list of all Drivers is given as as list

def print_drivers(drivers):
    for driver in drivers:
        print(driver)

# searches and prints the best lap time of the competition and the driver and team associated with it.
# A list of all Drivers is given as as list

def find_best_lap_time(drivers):
    best_lap_time = driver_module.Driver.LAPS_NOT_YET_DRIVEN
    best_drivers = []
    for driver in drivers:
        if driver.get_best_lap_time() < best_lap_time:
            best_lap_time = driver.get_best_lap_time()
            best_lap_time_string = driver.centiseconds_to_time_string(best_lap_time)
            best_drivers = [driver]
        elif driver.get_best_lap_time() == best_lap_time and driver.get_best_lap_time() < driver_module.Driver.LAPS_NOT_YET_DRIVEN:
            best_drivers.append(driver)
    if best_lap_time < driver_module.Driver.LAPS_NOT_YET_DRIVEN:
        print("The best lap time is {:s}".format(best_lap_time_string))
        print("It has been driven by:")
        for best_driver in best_drivers:
            print(best_driver.get_name())
    else:
        print("No laps driven by anyone.")

# Prints a menu and returns an integer representing the user's choice

def choose_action():
    print()
    print("Choose an action:")
    print("1. record a new lap time for a driver")
    print("2. correct and overwrite a previously recorded lap time of a driver")
    print("3. compare the best lap times of two drivers")
    print("4. print the drivers and their lap times")
    print("5. find the best lap time among all drivers")
    print("6. quit")
    choice = read_integer()
    return choice

def main():
    drivers = create_drivers(names=["Eetu Energisti", "Kati Konelainen", "Riina Raksalainen", "Keke Kemisti", "Sami Sahkolainen"],
                             teams=["Fast Alliance", "Motor Mikes", "Last and Furious", "Roadsters", "SpeedTeam"])
    user_choice = choose_action()
    while user_choice != 6:
        if user_choice == 1:
            record_a_lap_time(drivers)
        elif user_choice == 2:
            overwrite_lap_time(drivers)
        elif user_choice == 3:
            compare_two(drivers)
        elif user_choice == 4:
            print_drivers(drivers)
        elif user_choice == 5:
            find_best_lap_time(drivers)
        user_choice = choose_action()


main()
