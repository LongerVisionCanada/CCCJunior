if __name__ == "__main__":
    iStr = input()
    hStr = ":-)"
    sStr = ":-("

    l = len(iStr)

    if l < 3:
        print("none")
    else:
        nbOfHs = 0
        nbOfSs = 0
        for i in range(l - 3 + 1):
            if iStr[i : i + 3] == hStr:
                nbOfHs += 1
            elif iStr[i : i + 3] == sStr:
                nbOfSs += 1

        if nbOfHs == nbOfSs:
            if nbOfHs == 0:
                print("none")
            else:
                print("unsure")
        elif nbOfHs > nbOfSs:
            print("happy")
        else:
            print("sad")
