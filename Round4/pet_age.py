def dog_age_in_human_years(age):
    if age <= 1:
        age = age * 15

    elif age <= 2:
        age = 15 + (age - 1) * 9

    else:
        age = 15 + 9 + ((age - 2) * 5)

    print(f"Your dog is {age:.1f} years old in human years!")


def cat_age_in_human_years(age):
    if age <= 1:
        age = age * 15

    elif age <= 2:
        age = 15 + (age - 1) * 10

    else:
        age = 15 + 10 + ((age - 2) * 4)

    print(f"Your cat is {age:.1f} years old in human years!")


def bunny_age_in_human_years(age):
    if age <= 0.5:
        age = (age / 0.5) * 16

    elif age <= 1:
        age = 16 + ((age - 0.5) / 0.5) * 5

    else:
        age = 16 + 5 + (age - 1.0) * 6

    print(f"Your bunny is {age:.1f} years old in human years!")


def main():
    print("Welcome to the pet age calculator! I will tell your pet's age in human years.")
    choice = 0
    while not 1 <= choice <= 3:
        print("Choose a pet:\n"
              "1: dog\n"
              "2: cat\n"
              "3: bunny")
        choice = int(input())
    age = float(input("How old is your pet?\n"))
    if choice == 1:
        dog_age_in_human_years(age)
    elif choice == 2:
        cat_age_in_human_years(age)
    else:
        bunny_age_in_human_years(age)


main()
