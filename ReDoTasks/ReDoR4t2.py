def cul_dog_age(pet_age):
    first = 15
    second = 9
    constant = 5

    if pet_age <= 1:
        r = pet_age * first

    elif pet_age <= 2:
        r = first + (pet_age - 1) * second

    else:
        r = first + second + ((pet_age - 2) * constant)

    print(f"Your dog is {r:.1f} years old in human years!")


def cul_cat_age(pet_age):
    first = 15
    second = 10
    constant = 4

    if pet_age <= 1:
        r = pet_age * first

    elif pet_age <= 2:
        r = first * (pet_age - 1) * second

    else:
        r = first + second + ((pet_age - 2) * constant)

    print(f"Your cat is {r:.1f} years old in human years!")


def cul_bunny_age(pet_age):
    first_half = 16
    first_later_half = 5
    constant = 6

    if pet_age <= 0.5:
        r = (pet_age / 0.5) * first_half

    elif pet_age <= 1:
        r = first_half + ((pet_age - 0.5) / 0.5) * first_later_half

    else:
        r = first_half + first_later_half + ((pet_age - 1.0) * constant)

    print(f"Your bunny is {r:.1f} years old in human years!")


def main():
    print("Welcome to the pet age calculator! I will tell your pet's age in human years.")
    choice = int(input("Choose a pet:\n"
                   "1: dog\n"
                   "2: cat\n"
                   "3: bunny\n"))

    pet_age = float(input("How old is your pet?\n"))

    if choice == 1:
        cul_dog_age(pet_age)

    elif choice == 2:
        cul_cat_age(pet_age)

    elif choice == 3:
        cul_bunny_age(pet_age)

    else:
        print("error")


main()
