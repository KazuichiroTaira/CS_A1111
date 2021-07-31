from string import ascii_lowercase

VOWELS = ["a", "i", "u", "e", "o", "y"]


def compare_words(user_str, eng_word):
    dict_word_count = len(eng_word)
    user_word_count = len(user_str)

    if dict_word_count != user_word_count:
        return False

    for i in range(user_word_count):
        u_ch = user_str[i]
        e_ch = eng_word[i]

        if u_ch == "-":  # should be vowel
            if e_ch not in VOWELS:
                return False

        elif u_ch == "*":  # should be consonant
            if e_ch in VOWELS:
                return False

        elif u_ch == "_":  # can be anything
            pass

        else:
            if u_ch != e_ch:
                return False

    return True


def compare_w_eng_dict(eng_dict, user_str):

    possible_words = []

    for eng_word in eng_dict:

        eng_word = eng_word.strip()

        correct = compare_words(user_str, eng_word)

        if correct:
            possible_words.append(eng_word)

    return possible_words


def check_user_input(user_str):
    correct = True
    incorrect_ch = None
    for ch in user_str:

        if ch in ascii_lowercase:
            pass

        else:
            if ch not in ["-", "*", "_"]:

                incorrect_ch = ch
                correct = False
                break

    return correct, incorrect_ch


def main():
    filename = "words.txt"
    with open(filename, 'r') as f:
        eng_dict = f.readlines()

    print("Welcome to the crossword Generator! Discover Hidden words!\n"
          "_ = any letter\n"
          "* = any consonant\n"
          "- = any vowel\n"
          "Enter the word with all the known letters (eg 's___nt', '__- k', '*** _ ****'):")

    user_str = input("")
    user_str = user_str.lower()
    print()

    correct, inc_ch = check_user_input(user_str)
    if correct:
        possible_words = compare_w_eng_dict(eng_dict, user_str)
        n_pos = len(possible_words)
        if n_pos == 0:
            print('There were no matches :(')

        else:
            for word in possible_words:
                print(word)

            print(f"There were {len(possible_words)} matches.")
    else:
        print(f"Your word contains an incorrect character '{inc_ch}'")


main()