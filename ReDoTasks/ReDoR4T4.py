HORSEPOWER_IN_KW = 0.746
ERROR_WITH_CALCULATE_ENERGY = -99


def calculate_energy(power, power_unit, time, time_unit):

    if power_unit == "kW":
        power = power * 1000

    elif power_unit == "hp":
        power = power * HORSEPOWER_IN_KW

    else:
        pass

    if time_unit == "days":

        csm = power * time * 24 / 1000

    elif time_unit == "hours":

        csm = power * time / 1000

    elif time_unit == "minutes":
        csm = power * time / 60

    return csm

def calculate_energy_cost(energy_kwh, price_per_kwh):

    energy_cost = energy_kwh * price_per_kwh / 100

    return energy_cost



def main():
    print("Welcome to calculate the energy used by the Appliance and its cost!")
    p_unit = str(input("What unit to use for the power ('W', 'kW' or 'hp')?\n"))
    power = float(input(f"Enter the power of the Appliance in {p_unit}:\n"))
    t_unit = str(input(f"What unit to use for the time ('minutes', 'hours' or 'days')?\n"))
    time = float(input(f"Enter the time the Appliance is running in {t_unit}:\n"))
    # p_unit = "hp"
    # power = float(77)
    # t_unit = "minutes"
    # time = 45.0

    energy_kwh = calculate_energy(power, p_unit, time, t_unit)

    print(f"You have an Appliance of {power} {p_unit} running for {time} {t_unit}.\n"
          f"It consumes approximately {energy_kwh:.3g} kWh.")

    price_per_kwh = float(input("Enter the electricity price in cents / kWh:\n"))
    # price_per_kwh = 9.5

    energy_cost = calculate_energy_cost(energy_kwh, price_per_kwh)
    print(f"The energy will cost approximately {energy_cost:.2f} eur.")


main()