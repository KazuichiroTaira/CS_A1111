def main():
    line = input("Enter the patient's age in years:\n")
    x = int(line)
    line = input("Enter the patient's weight in kg:\n")
    y = float(line)
    if x < 3:
        d = None
    elif x < 9:
        dose = y * 10.0
        d = dose
        if d > 250.0:
            d = 250.0
    elif x < 31:
        dose = y * 10.0
        d = dose
        if d > 900.0:
            d = 900.0
    else:
        assert x >= 30, 'i did it wrong'
        dose = y * 13.0
        d = dose
        if d > 900.0:
            d = 900.0
    if d is None:
        print("You are not allowed to administer the drug.")
    else:
        print("You can administer a dose of", d, "mg of the drug ")
main()