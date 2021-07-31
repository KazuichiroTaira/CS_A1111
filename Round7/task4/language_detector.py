def sorted_by_values(dictionary):
    keys = list(dictionary)  # keys only by default
    sorted_dictionary = {}
    while len(keys) > 0:
        key_with_lowest_value = keys[0]
        for key in keys:
            if dictionary[key] < dictionary[key_with_lowest_value]:
                key_with_lowest_value = key
        keys.remove(key_with_lowest_value)
        # add to dictionary, stays in order
        sorted_dictionary[key_with_lowest_value] = dictionary[key_with_lowest_value]
    return sorted_dictionary


def convert_percentage_text_to_proportion(text):
    black_list = ["~", "%"]

    for e in black_list:
        text = text.replace(e, "")

    num = float(text)
    num *= 0.01
    return num


def read_letter_freq(filename):
    file = open(filename, 'r', encoding='utf-8')
    file_letter_frequencies_string = file.read()
    file.close()
    # print(type(file_letter_frequencies_string))

    readline = file_letter_frequencies_string.splitlines()
    # print(type(readline))

    first_line = readline[0]
    languages = first_line.split(";")
    languages.remove("Letter")
    # print(languages)

    dict_freq = {}
    # key as language and value as in other dictionary

    for lang in languages:
        dict_freq[lang] = {}

    for line in readline[1:]:
        list_line = line.split(";")
        letter = list_line[0]
        # print(letter)

        for i in range(len(languages)):
            str_freq = list_line[i + 1]
            freq = convert_percentage_text_to_proportion(str_freq)
            lang = languages[i]
            # print(f"{lang} = {freq}")
            dict_freq[lang][letter] = freq

    return dict_freq


def clean_text(text):
    text = text.lower()
    c_text = ""

    for e in text:
        if e.isalpha():
            c_text += e

    return c_text


def count_letters(text):
    freq_dict = {}

    for e in text:
        if e in freq_dict:
            freq_dict[e] += 1

        else:
            freq_dict[e] = 1

    total = 0
    for e in freq_dict:
        total += freq_dict[e]

    for e in freq_dict:
        freq_dict[e] /= total

    return freq_dict


def generate_frequency_dictionary(text):

    text = clean_text(text)
    freq_dict = count_letters(text)
    return freq_dict


def calculate_error_score(frequencies_of_known_language, observed_frequencies):

    all_letters = []
    for letter in frequencies_of_known_language:
        all_letters.append(letter)

    for letter in observed_frequencies:
        if letter not in all_letters:
            all_letters.append(letter)

    error_container = {}

    for letter in all_letters:

        if letter in frequencies_of_known_language:
            value_letter_lang = frequencies_of_known_language[letter]
        else:
            value_letter_lang = 0.0

        if letter in observed_frequencies:
            value_letter_obs = observed_frequencies[letter]
        else:
            value_letter_obs = 0.0

        error = abs(value_letter_lang - value_letter_obs)
        error_container[letter] = error

    total = 0
    for letter in error_container:
        total += error_container[letter]

    return total


def calculate_error_scores(letter_frequency_data, observed_frequencies):

    scores = {}

    for lang in letter_frequency_data:
        freq_lang = letter_frequency_data[lang]
        sc = calculate_error_score(freq_lang, observed_frequencies)
        scores[lang] = sc

    return scores


def main():
    filename = input("Enter the name of the letter frequency file\n")
    # filename = "letter_frequencies.txt"
    letter_frequency_data = read_letter_freq(filename)
    print("Letter frequency data read!")

    txt_file = input("Enter the name of the file containing the text to read:\n")
    # txt_file = "wikipedia_de_programming.txt"
    file = open(txt_file, 'r', encoding='utf-8')
    file_txt_string = file.read()
    file.close()

    observed_frequencies = generate_frequency_dictionary(file_txt_string)
    observed_frequencies = sorted_by_values(observed_frequencies)

    errors = calculate_error_scores(letter_frequency_data, observed_frequencies)
    errors = sorted_by_values(errors)
    print(f"\nThe text is probably in one of the following languages:")
    n = 2
    i = 0
    for lang in errors:
        err = errors[lang]
        print(f"{lang} (error score = {err:.3f})")
        i += 1
        if i == n:
            break


main()
