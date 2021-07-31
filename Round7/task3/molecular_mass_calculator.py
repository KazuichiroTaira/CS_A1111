def open_dic(filename):
    try:
        atomic_mass_file = open(filename, 'r')

    except:
        print(f"Error in reading the file '{filename}'. The program ends.")
        return False, {}

    atomic_mass_dic = {}

    for line in atomic_mass_file:
        atom_and_mass = line.strip()

        if atom_and_mass.count(':') == 1:
            split_atom_and_mass = atom_and_mass.split(":")
            atom = split_atom_and_mass[0]
            str_mass = split_atom_and_mass[1]

        else:
            print(f'Invalid line: {atom_and_mass}')
            continue

        try:
            mass = float(str_mass)

        except:
            print(f'Invalid atomic mass on a line: {atom_and_mass}')
            continue

        atomic_mass_dic[atom] = mass

    atomic_mass_file.close()
    return True, atomic_mass_dic


def main():

    filename = input("Enter the name of the file containing the atomic masses:\n")
    exists, atomic_mass_dic = open_dic(filename)

    if not exists:
        return

    while True:
        line = input("Enter the Molecular formula:\n")
        line_split = line.split("-")

        molecular_mass = 0
        correct = True

        for atom_and_vol in line_split:

            if atom_and_vol.count(":") == 0:
                atom = atom_and_vol
                vol = 1

            elif atom_and_vol.count(":") == 1:

                atom_and_vol_split = atom_and_vol.split(":")
                atom = atom_and_vol_split[0]
                str_vol = atom_and_vol_split[1]
                try:
                    vol = int(str_vol)

                except:
                    correct = False
                    print("Invalid molecular formula.")
                    break

            else:
                correct = False
                print("Invalid molecular formula.")
                break

            if atom in atomic_mass_dic:
                read_from_dic = atomic_mass_dic[atom]
                molecular_mass += vol * read_from_dic

            else:
                correct = False
                print(f"Missing the atomic mass of this element: {atom}")
                break

        if correct:

            print(f"The molecular mass of {line} equals {molecular_mass:.2f} amu.")

        line = input("Continue? (y/n):\n")
        answer = line.lower()

        if answer == "y":
            continue

        else:
            print("The program ends.")
            break


main()