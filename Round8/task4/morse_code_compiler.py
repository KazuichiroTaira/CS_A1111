# Y1 SUMMER 2021
# Basic Course in Programming Y1
# Author: Joel Lahenius
# Template for Exercise 8.4

CHARACTER_TO_MORSE_STRING = {'0': '-----', '1': '.----', '2': '..---',
                             '3': '...--', '4': '....-',
                             '5': '.....', '6': '-....', '7': '--...',
                             '8': '---..', '9': '----.',
                             'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                             'E': '.', 'F': '..-.',
                             'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                             'K': '-.-', 'L': '.-..',
                             'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                             'Q': '--.-', 'R': '.-.', 'S': '...',
                             'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                             'X': '-..-', 'Y': '-.--', 'Z': '--..',
                             '.': '.-.-.-', ',': '--..--',
                             '?': '..--..', '!': '-.-.--',
                             '-': '-....-', '\'': '.----.'}


MORSE_TO_CHARACTER = {v: k for k, v in CHARACTER_TO_MORSE_STRING.items()}


def text_to_morse(text):
    """
    Converts text to morse code. Replaces unknown characters with '???' silently.
    Parameter text: str
    returns: str of morse words separated by "/", letters separated by spaces
    E.g.

    > text_to_morse("The quick brown fox jumps over the lazy dog")
    > '- .... . / --.- ..- .. -.-. -.- / -... .-. --- .-- -. / ..-. --- -..- / .--- ..- -- .--. ... / --- ...- . .-. / - .... . / .-.. .- --.. -.-- / -.. --- --.'

    > text_to_morse("The $uick #r#wn")
    > '- .... . / ??? ..- .. -.-. -.- / ??? .-. ??? .-- -.'

    > text_to_morse("tropical")
    > '- .-. --- .--. .. -.-. .- .-..'

    > text_to_morse("")
    > ''
    """
    translation = ""
    words = text.split(" ")
    for word in words:

        if translation != "":
            translation += " / "

        for ch in word:
            try:
                tr_ch = CHARACTER_TO_MORSE_STRING[ch.upper()]
            except KeyError:
                tr_ch = "???"
            translation += tr_ch
            translation += " "
        translation = translation[:-1]

    return translation.lower()


def morse_to_text(morsecode):
    """
    Converts morsecode to text. Replaces unknown morse strings with '?' silently.
    Parameter morsecode: string. Words separated by "/", letters by spaces.
    returns: str

    E.g.
    > morse_to_text("- .... . / --.- ..- .. -.-. -.- / -... .-. --- .-- -. / ..-. --- -..- / .--- ..- -- .--. ... / --- ...- . .-. / - .... . / .-.. .- --.. -.-- / -.. --- --.")
    > 'the quick brown fox jumps over the lazy dog'

    > morse_to_text("- .... . / .-..-.-.-.-. ..- .. -.-. -.- / ......- .-. --..--.. .-- -.")
    > 'the ?uick ?r?wn'

    > morse_to_text("")
    > ''
    """
    # your code here
    translation = ""
    words = morsecode.split("/")
    for word in words:
        if translation != "":
            translation += " "
        characters = word.split(" ")
        for ch in characters:
            if ch == "":
                continue
            try:
                tr_ch = MORSE_TO_CHARACTER[ch]
            except KeyError:
                tr_ch = "?"
            translation += tr_ch
    return translation.lower()


def main():

    print(
        "This program converts text to international morse code and vice versa")
    print(
        "Type\n'mt' to convert morse code to plaintext\n'tm' to convert plaintext to morse code")
    mode = input("")

    if mode == "tm":
        func = text_to_morse
        end = "morse"
        tr_name = "morse code"
        input_name = "text"
    elif mode == "mt":
        func = morse_to_text
        end = "translated"
        tr_name = "normal text"
        input_name = "morse code"
    else:
        print("Unknown choice. The program ends.")
        return

    print(f"Enter the name of the file containing the {input_name} to convert:")
    filename = input("")

    try:
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error reading the file.")
        return

    root = filename.split('.')[0]
    f2name = f"{root}_{end}.txt"

    tr_lines = ""
    count = 0
    for line in lines:
        line = line.strip()
        tr = func(line)

        tr_lines += f"{tr}\n"
        count += 1

    print(f'Your text contains {count} lines.')

    with open(f2name, "w") as f2:
        f2.write(tr_lines)

    print(f"The equivalent {tr_name} was written to the file {f2name}")


main()