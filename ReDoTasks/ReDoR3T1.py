

def main():
    line = input("This program will print a triangular pattern.\nWhat size should the pattern be?\n")
    size = int(line)
    # size = 7

    line = input("What character(s) should be used?\n")
    ch = str(line)
    # ch = str("#")

    c = 0

    for i in range(0, size):
        c += 1
        print(ch * c)

        if c == size:
            size += -1
            c += -1

            # print(size, c, "pass here")
            # while c <= size:
            #     print(ch * c)
            #     c = c - 1
            #
            #     if c == 0:
            #         break

            for i_2 in range(size):
                print(ch * c)
                # print(ch * i)
                c += -1


main()