def main():
    filename = input("Enter the name of the file to be read:\n ")
    # filename = "batch_short.txt"
    save_measure = []
    try:
        product_file = open(filename, 'r')
        total = 0.0
        count = 0
        for line in product_file:
            line = line.rstrip()
            measure = float(line)
            save_measure.append(measure)
            total += measure
            count += 1
        product_file.close()

        print("File read successfully.")

        if count == 0:
            print("The file did not contain any data.")

        else:
            # print("The file contained {: d} values, average {: .2f}".format(count, total / count))
            # print(save_measure)

            count_optimal = 0
            count_allowed = 0
            count_faulty = 0

            for e in save_measure:

                if 4.52 <= e <= 4.58:  # BATCH_QUALITY["Optimal dimension"]:
                    count_optimal += 1

                elif 4.50 <= e <= 4.60:
                    count_allowed += 1

                else:
                    count_faulty += 1

            # count_optimal, count_allowed, count_faulty = quality_control(save_measure)

            racio_optimal = count_optimal / count * 100
            racio_allowed = count_allowed / count * 100
            racio_faulty = count_faulty / count * 100

            print(f"The batch contained:\n"
                  f"{count_optimal} optimal ({racio_optimal:.1f}%)\n"
                  f"{count_allowed} allowed ({racio_allowed:.1f}%)\n"
                  f"{count_faulty} faulty ({racio_faulty:.1f}%).")

            if racio_faulty > 3.00:
                print("The batch didn't pass the quality inspection. ")

            else:
                print("The batch passed the quality inspection. ")


    except OSError:
        print(f"Error in reading the file '{filename:s}'. Program ends.")

    except ValueError:
        print(f"Incorrect number in the file '{filename:s}'. Program ends.")


main()
