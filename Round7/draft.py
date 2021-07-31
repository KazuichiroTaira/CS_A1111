# # # save_measure = [4.56, 4.62, 4.51, 4.55, 4.53, 4.5, 4.58]
# #
# # # for e in save_measure:
# # #     print(e)
# # #     if 4.52 <= e <= 4.58:  # BATCH_QUALITY["Optimal dimension"]:
# # #         # count_optimal += 1
# # #         print("opt")
# # #
# # #     elif 4.50 <= e <= 4.60:
# # #         # count_allowed += 1
# # #         print("alwed")
# # #
# # #     else:
# # #         # count_faulty += 1
# # #         print("faulty")
# #
# # def quality_control(save_measure):
# #     count_optimal = 0
# #     count_allowed = 0
# #     count_faulty = 0
# #
# #     for e in save_measure:
# #
# #         if 4.52 <= e <= 4.58:  # BATCH_QUALITY["Optimal dimension"]:
# #             count_optimal += 1
# #
# #         elif 4.50 <= e <= 4.60:
# #             count_allowed += 1
# #
# #         else:
# #             count_faulty += 1
# #
# #     return count_optimal, count_allowed, count_faulty
# #
# #
# # count_optimal, count_allowed, count_faulty = quality_control([4.56, 4.62, 4.51, 4.55, 4.53, 4.5, 4.58])
# #
# # print(count_optimal)
# # print(count_allowed)
# # print(count_faulty)
# #
# #
# # # BATCH_QUALITY = {"Optimal dimension": 4.55,
# # #                  "Optimal variation": 0.03,
# # #                  "Permitted variation": 0.05}
# #
# # # def quality_control(save_measure):
# # #
# # #     count_optimal = 0
# # #     count_allowed = 0
# # #     count_faulty = 0
# # #
# # #     for e in save_measure:
# # #
# # #         if 4.52 <= e <= 4.58:  # BATCH_QUALITY["Optimal dimension"]:
# # #             count_optimal += 1
# # #
# # #         elif 4.50 <= e <= 4.60:
# # #             count_allowed += 1
# # #
# # #         else:
# # #             count_faulty += 1
# # #
# # #     return count_optimal, count_allowed, count_faulty
# #
# # a = [1, 2, 3]
# # while True:
# #
# #     b_str = input("give num")
# #     try:
# #         b = int(b_str)
# #         a.index(b)
# #         print(f"found {b}")
# #
# #     except ValueError:
# #         print(f"Not found {b_str}")
#
#
# def check_if_exists(word, words):
#     if word in words:
#         found = True
#     else:
#         found = False
#     return found
#
#
# def extract_eng_dic(filename):
#
#     eng_dictionary = open(filename, 'r')
#
#     words = []
#
#     for line in eng_dictionary:
#
#         word = line.strip()
#         words.append(word)
#
#     return words
#
#
# def main():
#
#     filename = "words.txt"
#     eng_words = extract_eng_dic(filename)
#     print(eng_words)
#     #user_word = "fox"
#     #result = check_if_exists(user_word, eng_words)
#     #print(result)
#
#
# main()
#
#
# def extract_atomic_mass(filename):
#     atomic_mass_file = open(filename, 'r')
#     # atomic_mass2 = open(filename2, 'r')
#
#     atomic_mass_dic = {}
#     # atomic_mass_dic2 = {}
#     try:
#         for line in atomic_mass_file:
#             atom_and_mass = line.strip()
#             split_atom_and_mass = atom_and_mass.split(":")

            # atom_as_key, mass_as value = atom_and_mass.split(":")
#             atom_as_key = split_atom_and_mass[0]
#             mass_as_value = float(split_atom_and_mass[1])
#             atomic_mass_dic[atom_as_key] = mass_as_value
#
#             # print(split_atom_and_mass)
#             # print(atom_as_key, mass_as_value)
#         atomic_mass_file.close()
#         print(atomic_mass_dic)

    # for line in atomic_mass2:
    #     atom_and_mass = line.strip()
    #     split_atom_and_mass_or_extra = atom_and_mass.split(":" or "")
    #     # print(split_atom_and_mass_or_extra)
    #
    #     if len(split_atom_and_mass_or_extra) == 1:
    #         split_atom_and_mass_or_extra.append("")
    #         split_atom_and_mass_or_extra.append("")
    #
    #     elif len(split_atom_and_mass_or_extra) == 2:
    #         split_atom_and_mass_or_extra.append("")
    #
    #     else:
    #         pass
    #
    #
    #     atom_as_key = split_atom_and_mass_or_extra[0]
    #     mass_as_value = split_atom_and_mass_or_extra[1]
    #     extra_info = split_atom_and_mass_or_extra[2]
    #     atomic_mass_dic2[atom_as_key] = mass_as_value, extra_info
    #     # atomic_mass_dic2[atom_as_key: mass_as_value] = extra_info   <- TypeError: unhashable type: 'slice'
    #
    # atomic_mass2.close()
    # print(atomic_mass_dic2)


    # return atomic_mass_dic1, atomic_mass_dic2


def main():
    # open and store the list of atomic mass from two files.
    # filename = input("Enter the name of the file containing the atomic masses:\n")
    filename = "task3/atomic_masses2.txt"
    atomic_mass_file = open(filename, 'r')
    # print(f'{filename} is open')

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

        # print(split_atom_and_mass)
        # print(atom_as_key, mass_as_value)
    atomic_mass_file.close()
    # print(atomic_mass_dic)

    ### user's input ###

    line = input("Enter the Molecular formula:\n")
    line_split = line.split("-")
    # print(line_split)

    molecular_mass = 0

    for atom_and_vol in line_split:
        # print(atom_and_vol)

        if ":" in atom_and_vol:
            # print(atom_and_vol, ":")
            atom_and_vol_split = atom_and_vol.split(":")
            atom_as_key = atom_and_vol_split[0]

            vol_as_int_value = int(atom_and_vol_split[1])
            read_from_dic = atomic_mass_dic[atom_as_key]
            molecular_mass += vol_as_int_value * read_from_dic
            # print(read_from_dic)
            # print(vol_as_int_value)
            # print(molecular_mass, ":")

        else:
            # print(atom_and_vol, "single")
            molecular_mass = atomic_mass_dic[atom_and_vol] + molecular_mass
            # print(atomic_mass_dic[atom_and_vol])
            # print(molecular_mass, "single")

    print(f"{molecular_mass:.2f}")


main()