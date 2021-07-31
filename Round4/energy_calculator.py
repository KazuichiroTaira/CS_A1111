a_horsepower_in_kw = 0.746
W_in_kW = 1 / 1000

error_with_calculate_energy = -99
days_in_hours = 24
min_in_hours = 1 / 60

price_conversion = 0.01


def calculate_energy(power, power_unit, time, time_unit):
    if power < 0 \
            or time_unit not in ('minutes', 'hours', 'days') \
            or time < 0 \
            or power_unit not in ('W', 'kW', 'hp'):

        return error_with_calculate_energy

    if power_unit == "W":

        if time_unit == "days":
            r_cal_energy_as_kWh = power * time * days_in_hours * W_in_kW

        elif time_unit == "hours":
            r_cal_energy_as_kWh = power * time * W_in_kW

        else:
            r_cal_energy_as_kWh = power * time * min_in_hours * W_in_kW

    elif power_unit == "kW":

        if time_unit == "days":
            r_cal_energy_as_kWh = power * time * days_in_hours

        elif time_unit == "hours":
            r_cal_energy_as_kWh = power * time

        else:
            r_cal_energy_as_kWh = power * time * min_in_hours

    else:  # power_unit == "hp":  # the energy_units in hp - horsepower!!

        if time_unit == "days":
            r_cal_energy_as_kWh = power * time * days_in_hours * a_horsepower_in_kw

        elif time_unit == "hours":
            r_cal_energy_as_kWh = power * time * a_horsepower_in_kw

        else:
            r_cal_energy_as_kWh = power * time * min_in_hours * a_horsepower_in_kw

    return r_cal_energy_as_kWh


def calculate_energy_cost(energy_kwh, price_per_kwh):
    r_cal_ene_cost = energy_kwh * price_per_kwh
    return r_cal_ene_cost


def main():
    print("Welcome to calculate the energy used by the appliance and its cost!")
    line = input("What unit to use for the power ('W', 'kW' or 'hp')?\n")
    power_unit = str(line)

    line = input(f"Enter the power of the appliance in {power_unit:}:\n")
    power = float(line)

    line = input("What unit to use for the time ('minutes', 'hours' or 'days')?\n")
    time_unit = str(line)

    line = input(f"Enter the time the appliance is running in {time_unit:}:\n")
    time = float(line)

    r_cal_energy_as_kWh = calculate_energy(power, power_unit, time, time_unit)
    print(f"\nYou have an appliance of {power:} {power_unit:} running for {time:} {time_unit:}.")

    if r_cal_energy_as_kWh == error_with_calculate_energy:
        print("You have entered some invalid values.")

    else:
        print(f"It consumes approximately {r_cal_energy_as_kWh:.3g} kWh.\n")

        line = input("Enter the electricity price in cents/kWh:\n")
        price_per_kwh = float(line)
        r_cal_ene_cost = calculate_energy_cost(r_cal_energy_as_kWh, price_per_kwh)
        print(f"The energy will cost approximately {r_cal_ene_cost * price_conversion:.2f} eur.")


main()
