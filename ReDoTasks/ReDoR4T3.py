import math

G = 9.81
RHO = 1.2
CD_HUMAN = 1.0
CD_BOX = 2.0


def calculate_terminal_velocity(mass, projected_area, drag_coefficient):
    weight = calculate_weight(mass)
    v_t = math.sqrt((2 * weight) / (RHO * projected_area * drag_coefficient))
    return v_t


def calculate_weight(mass):
    weight = mass * G
    return weight


def main():

    hmn_mass = float(input("Enter the mass of a human in kg:\n"))
    hmn_area = float(input("Enter the projected area the human in m ^ 2:\n"))

    v_t_h = calculate_terminal_velocity(hmn_mass, hmn_area, CD_HUMAN)

    print(f"The human's terminal velocity: {v_t_h:.2f} m / s\n")
    # print(f"{weight_h:.1f}")

    box_mass = float(input("Enter the mass of a box in kg:\n"))
    box_area = float(input("Enter the projected area of the box in m ^ 2:\n"))

    v_t_b = calculate_terminal_velocity(box_mass, box_area, CD_BOX)

    print(f"The box's terminal velocity: {v_t_b:.2f} m / s")
    # print(f"{weight_b:.1f}")

    if v_t_h > v_t_b:
        print("The terminal velocity of the human is higher.")

    elif v_t_h == v_t_b:
        print("The terminal velocity of the human and box are the same.")

    else:
        print("The terminal velocity of the box is higher.")


main()