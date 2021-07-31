def check_if_exists(word, words):
    word_lower = word.lower()
    if word_lower in words:
        found = True
    else:
        found = False
    return found


def extract_eng_dic(filename):

    eng_dictionary = open(filename, 'r')

    words = []

    for line in eng_dictionary:
        word = line.strip()
        words.append(word)

    eng_dictionary.close()

    return words


def main():
    filename = "words.txt"
    eng_words = extract_eng_dic(filename)

    # Collect user data -------------------------------------------------------
    print("Enter the text to be spell-checked (empty line to end input).")

    saved_split_line = []

    while True:
        line = input("")
        split_line = line.split(" ")

        if line == "":
            break
        else:
            saved_split_line.append(split_line)

    print()

    # Treat user data -------------------------------------------------------
    print("Checked text, typos highlighted with '*'")

    typo = 0

    for user_line in saved_split_line:

        display_list = ['>>', ]
        for word in user_line:
            found = check_if_exists(word, eng_words)

            if found:
                to_add = f"{word}"
            else:
                to_add = f"*{word}*"
                typo += 1

            display_list.append(to_add)

        display = ' '.join(display_list)
        print(display)

    if typo == 0:
        print("The text was clean.")

    else:
        print(f"There were {typo} typos.")


main()
