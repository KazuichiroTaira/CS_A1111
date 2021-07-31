import math

g = 9.81  # the acceleration of fall, ie a constant 9.81 m / s 2 near the Earth's surface.
rho_air = 1.2  # the density of the substance through which it is dropped. Here is air with a density of 1.2 kg / m^3
cd_human = 1.0  # c_d is the drag coefficient we assume is 1.0 for a person and 2.0 for a box.
cd_box = 2.0


def calculate_terminal_velocity(mass, projected_area, drag_coeff):
    w = calculate_weight(mass)
    t_v = math.sqrt((2 * w) / (rho_air * projected_area * drag_coeff))
    return t_v


def calculate_weight(mass):
    cw = mass * g
    return cw


def main():
    line = input("Enter the mass of a human in kg:\n ")
    mass_human = float(line)

    line = input("Enter the projected area of the human in m^2:\n")
    pro_ar_human = float(line)

    v_t_h = calculate_terminal_velocity(mass_human, pro_ar_human, cd_human)
    print(f"The human's terminal velocity: {v_t_h:.2f} m / s\n")

    line = input("Enter the mass of a box in kg:\n")
    mass_box = float(line)

    line = input("Enter the projected area of the box in m^2:\n")
    pro_ar_box = float(line)

    v_t_b = calculate_terminal_velocity(mass_box, pro_ar_box, cd_box)

    print(f"The box's terminal velocity: {v_t_b:.2f} m / s\n")

    if v_t_h > v_t_b:
        print("The terminal velocity of the human is higher.")
    elif v_t_h == v_t_b:
        print("The terminal velocity of the human and box are equal.")
    else:
        print("The terminal velocity of the box is higher.")


main()
