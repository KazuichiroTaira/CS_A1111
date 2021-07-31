import datetime


def main():

    filename = input("Enter the name of the file to be created for your screen time data:\n")
    with open(filename, 'w'):
        pass

    start_date = input("Enter the start date in format 'DD.MM.YYYY': \n")

    str_day, str_month, str_year = start_date.split(".")
    day, month, year = int(str_day), int(str_month), int(str_year)
    date = datetime.date(day=day, month=month, year=year)

    print("Enter your screen watching time for each day (in minutes) in the format "
          "'[Phone minutes] [PC minutes] [TV minutes] [other minutes]'")

    total = 0
    num_days = 0
    while True:
        user_input = input(f"Enter your screen time on {date}: ")

        if user_input == "":
            break

        phone, pc, tv, other = user_input.split(" ")
        phone, pc, tv, other = int(phone), int(pc), int(tv), int(other)
        total += phone + pc + tv + other

        content = f"{date.year:04d}-{date.month:02d}-{date.day:02d}: {phone}/{pc}/{tv}/{other}\n"

        with open(filename, 'a') as output_file:
            output_file.write(content)

        date += datetime.timedelta(days=1)
        num_days += 1

    print("-"*100)
    print(f"Screen times saves succesfully in the file {filename}\n"
          f"Saved the screen times of {num_days} days.")

    if num_days > 0:
        total_hour = total / 60
        avg_hour = total_hour / num_days
        print(f"Total screen time from this period is {total_hour:.1f} hours and daily average is {avg_hour:.1f} hours.")

    print("\nLet's look inside the file. It looks as follows:")
    print("-" * 100)

    with open(filename, 'r') as output_file:
        all_line = output_file.read()

    all_line = all_line.splitlines()

    for line in all_line:
        print(line)

main()