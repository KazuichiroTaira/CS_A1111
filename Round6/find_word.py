# Y1 SUMMER 2021
# Basic Course in Programming Y1
# Author: Joel Lahenius
# Template for Exercise 6.2

def find_indices(string, word):
    """
    returns the first indices in 'string' that form (in order) the substring 'word'

    returns True, list of indices
    - if all of the letters in 'word' were found in order

    returns False, list of indices as far as matches were found
    - if none or only some of the letters in 'word' were found in order

    e.g.

    > find_indices("esmeirkki", "sei")
    > (True, [1, 4, 8])

    > find_indices("esimerkki", "side")
    > (False, [1, 2])
    """
    # implement your code here!
    indices = []
    all_found = False

    if len(word) == 0:
        return True, []

    pos = 0
    target = word[pos]

    for i in range(len(string)):
        s = string[i]

        if s == target:
            indices.append(i)
            pos += 1

            if pos < len(word):
                target = word[pos]

            else:
                all_found = True
                break


    return all_found, indices


def find_indices_ignore_case(string, word):
    """
    finds the indices of 'word' in 'string in order - exactly like in 'find_indices',
    except the case of the letters is ignored
    """
    # implement your code here!

    new_word = word.lower()
    new_string = string.lower()
    return find_indices(new_string, new_word)


def main():
    # examples to test your functions
    example_cases = (
        ("esimerkki", ""),
        ("esimerkki", "sei"),
        ("esimerkki", "kis"),
        ("iiiieeee", "iieee"),
        ("iiiieeee", "iei"),
        ("iiiieeee", "ieeiiee"),
        ("esimerkki", "esmerki"),
        ("Lorem ipsum dolor sit amet", "ohjelmointi"),
        ("Lorem ipsum dolor sit amet, consectetur adipiscing elit", "on ohjelmointi on kivaa"),
        ("Lorem ipsum dolor sit amet, consectetur adipiscing elit", "meri")
    )
    for example_string, example_word in example_cases:
        print("find_indices('{:s}', '{:s}') \nreturned {}\n".format(example_string, example_word,
                                                                    find_indices(example_string, example_word)))

    print('find_indices("EsIMERKKITEKSTI", "SeiTi") \nreturned', find_indices("EsIMERKKITEKSTI", "SeiTi"))
    print('\nfind_indices_ignore_case("EsIMERKKITEKSTI", "SeiTi") \nreturned',
          find_indices_ignore_case("EsIMERKKITEKSTI", "SeiTi"))


main()
