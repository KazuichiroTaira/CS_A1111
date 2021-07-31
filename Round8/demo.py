import math


def main():
    print("The program calculates the areas of the circles and saves them ")
    print("They are in a file.")
    name = input("Enter the name of the file to write: ")
    try:
        output_file = open(name, "w")
        output_file.write("rain area\n")
        print("Enter the circles, stop with a negative.")
        rain = 0.0  # initial value for the while cascade condition
        while rain >= 0.0:
            row = input()
            try:
                rain = float(row)
                if rain >= 0.0:
                    area = math.pi * rain * rain
                    output_file.write(f"{rain: <7.2f} {area: <10.2f}\n")

            except ValueError:
                print("Error: rain must be a decimal number.")

        output_file.close()
        print("Results have been written to file", name)

    except OSError:
        print("Error writing file", name, "The program terminates.")


main()