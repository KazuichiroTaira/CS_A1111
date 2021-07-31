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


def main():
    # # filename = input("Enter the name of the letter frequency file\n")
    filename = "letter_frequencies.txt"



main()
