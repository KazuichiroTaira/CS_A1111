
# def trip():
#     print("This program will print a triangular pattern.")
#     line = input("What size should the pattern be?\n")
#     s = int(line)
#     c = input("What character(s) should be used?\n")
#     x = (2 * s) - 1
#     for i in range(x):
#         x = s * c
#         print(x)
# trip()

def main():
    print("This program will print a triangular pattern.")
    line = input("What size should the pattern be?\n")
    n = int(line) + 1
    c = input("What character(s) should be used?\n")
    m = n - 2
    for i in range(0, n, 1):
        r = c * i
        print(r)
    for i in range(m, 0, -1):
        p = c * i
        print(p)
main()

