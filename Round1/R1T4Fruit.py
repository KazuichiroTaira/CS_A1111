def f():
    line = input("How much money do you have?\n")
    cash = float(line)
    nb = cash / (170 * (1.49 / 1000))
    na = cash / (170 * (2.49 / 1000))
    no = cash / (270 * (1.99 / 1000))
    print("you can buy", int(nb), "bananas.")
    print("you can buy", int(na), "apples.")
    print("you can buy", int(no), "oranges.")
f()