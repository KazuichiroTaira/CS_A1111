DATA_SIZE = {
    "Drink size": ["mini", "small", "medium", "large", "xl"],
    "Milliliters": [125, 200, 350, 500, 650],
    "Base price": [2.00, 2.75, 4.50, 5.50, 6.00]}

DATA_ING = {
    "Ingredient": [
        "pear", "banana", "strawberry", "coconut", "kiwi", "guava", "lingonberry",
        "dragonfruit", "bilberry", "cloudberry"],
    "Price multiplier": [0.7, 0.7, 1.0, 1.0, 1.0, 1.3, 1.3, 1.5, 1.5, 2.0]}

DATA_TYPE = {
    "Drink types": ["juice", "smoothie", "milkshake"],
    "Extra fee": [0.00, 0.50, 1.00]}

N_ARG = 3


def check_drink(drink_string):

    drink_list = drink_string.split(" ")
    if len(drink_list) != N_ARG:
        error_msg = f"Invalid input, {len(drink_list)} parts found, 3 expected"
        return False, error_msg

    ds = DATA_SIZE["Drink size"]
    ordered_size = drink_list[0]
    if ordered_size.lower() not in ds:
        error_msg = f'Invalid size: {ordered_size}'
        return False, error_msg

    il = DATA_ING["Ingredient"]
    ing_str = drink_list[1]
    ing_list = ing_str.split("-")
    for e in ing_list:
        if e.lower() not in il:
            error_msg = f'Invalid ingredient: {e}'
            return False, error_msg

    dt = DATA_TYPE["Drink types"]
    ordered_type = drink_list[2]
    if ordered_type.lower() not in dt:
        error_msg = f'Invalid drink type: {ordered_type}'
        return False, error_msg

    return True, ''


def calculate_ingredients_price_multiplier(ingredients):

    pm_list = []

    for e in ingredients:
        # for i in range(len(DATA_ING['Ingredient'])):
        #    if DATA_ING['Ingredient'][i] == e:
        #         pm = DATA_ING['Price multiplier'][i]
        i = DATA_ING['Ingredient'].index(e.lower())
        pm = DATA_ING['Price multiplier'][i]
        pm_list.append(pm)

    return sum(pm_list) / len(pm_list)


def main():
    print("Welcome to Clean Natural Superfood Exotic Drinks vending machine!\n"
          "Enter your order. Stop with an empty line.\n"
          "[size] [ingredient1-ingredient2-...] [milkshake/smoothie/juice]")

    ordering_list = []
    drink_string = "anything"

    while drink_string != "":
        drink_string = input("Enter your next drink:\n")
        if drink_string == "":
            break

        correct, error_msg = check_drink(drink_string)

        if not correct:
            print(error_msg)

        else:
            ordering_list.append(drink_string)

    total_price = 0.0

    for drink_string in ordering_list:

        ordered_size, ingredient_string, ordered_type = drink_string.split(' ')
        ingredients = ingredient_string.split('-')

        i = DATA_SIZE["Drink size"].index(ordered_size.lower())
        bp = DATA_SIZE['Base price'][i]

        ing_pm = calculate_ingredients_price_multiplier(ingredients)

        i = DATA_TYPE["Drink types"].index(ordered_type.lower())
        ef = DATA_TYPE["Extra fee"][i]

        price = bp * ing_pm + ef
        print(f'{drink_string:.<80s} {price:>5.2f}')

        total_price += price

    print(f'{"":=<86s}\n{"Total":.<80s} {total_price:>5.2f}')


main()
