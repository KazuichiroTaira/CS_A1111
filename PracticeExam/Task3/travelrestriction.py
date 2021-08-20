def error_check(line):
    try:
        num_check = line[1:]

    except IndexError:
        return True

    for number in num_check:

        try:
            _ = int(number)

        except ValueError:
            return True

    return False


def cal_ratio(inhabitant, cases):
    per_100ths = 100000

    ratio_per_100ths = cases / inhabitant * per_100ths

    return ratio_per_100ths


def travel_rest_def(ratio_per_100ths):
    travel_rest = 1

    if ratio_per_100ths >= 8:
        travel_rest = 2

    else:
        pass

    return travel_rest


def main():
    filename = input("Enter the name of the file to be read:\n ")
    # filename = "statistics2.txt"
    open_file = open(filename, 'r')
    amount = []

    for line in open_file:
        line = line.strip()

        if line == "":
            print(f"Incorrect line: {line}")

        try:
            content = line.split(",")

        except ValueError:
            print(f"Incorrect line: {line}")
            continue

        error = error_check(content)

        if error:
            print(f"Incorrect number in line: {line}")
            continue

        try:
            country = content[0]
            inhabitant = int(content[1])
            cases = int(content[2])

        except IndexError:
            print(f"Incorrect number in line: {line}")
            continue

        ratio_per_100ths = cal_ratio(inhabitant, cases)

        travel_rest = travel_rest_def(ratio_per_100ths)

        amount.append(travel_rest)

        if travel_rest == 2:
            print(f"{country:s} ({ratio_per_100ths:.1f} cases per 100000 inhabitants): travel restrictions apply.")

        else:
            print(f"{country:s} ({ratio_per_100ths:.1f} cases per 100000 inhabitants): no travel restrictions.")

    if amount.count(2) < 0:
        print(f"Travel restrictions apply to {amount.count(2):d} countries.")

    else:
        print("")


main()
