import datetime


def main():
    with open("test.txt", 'r') as output_file:
        all_line = output_file.read()

    all_line = all_line.splitlines()

    for line in all_line:
        print(line)



main()
