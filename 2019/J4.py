if __name__ == "__main__":
    ops = input()

    hs = 0
    vs = 0
    for c in ops:
        if c == "H":
            hs += 1
        else:
            vs += 1

    if hs % 2 == 0 and vs % 2 == 0:
        print(str(1) + " " + str(2))
        print(str(3) + " " + str(4))
    elif hs % 2 == 1 and vs % 2 == 0:
        print(str(3) + " " + str(4))
        print(str(1) + " " + str(2))
    elif hs % 2 == 0 and vs % 2 == 1:
        print(str(2) + " " + str(1))
        print(str(4) + " " + str(3))
    else:
        print(str(4) + " " + str(3))
        print(str(2) + " " + str(1))
