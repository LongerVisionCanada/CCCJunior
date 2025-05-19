if __name__ == "__main__":
    P = input()
    D = input()

    # frequency array
    freqP = [0] * 26
    freqD = [0] * 26

    # [0, 25]
    for c in P:
        freqP[ord(c) - ord("a")] += 1
    for c in D:
        freqD[ord(c) - ord("a")] += 1

    # print(freqP)
    # print(freqD)

    sillykey = ""
    wrongkey = ""
    quietkey = ""
    if len(P) == len(D):
        for i in range(26):
            if freqP[i] > 0 and freqD[i] == 0:
                sillykey = chr(i + ord("a"))
            elif freqP[i] == 0 and freqD[i] > 0:
                wrongkey = chr(i + ord("a"))
        print(sillykey + " " + wrongkey)
        print("-")
    else:
        tmpKeys = []
        for i in range(26):
            if freqP[i] == 0 and freqD[i] > 0:
                wrongkey = chr(i + ord("a"))
            elif freqP[i] > 0 and freqD[i] == 0:
                tmpKeys.append(chr(i + ord("a")))

        # assume: tmpKeys[0] is sillykey
        P = P.replace(tmpKeys[0], wrongkey)
        P = P.replace(tmpKeys[1], "")

        if P == D:
            sillykey = tmpKeys[0]
            quietkey = tmpKeys[1]
        else:
            sillykey = tmpKeys[1]
            quietkey = tmpKeys[0]

        print(sillykey + " " + wrongkey)
        print(quietkey)
