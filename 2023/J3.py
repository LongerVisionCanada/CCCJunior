if __name__ == "__main__":
    N = int(input())

    dayYes = [0] * 5

    for i in range(N):
        s = input()
        for d in range(5):
            if s[d] == "Y":
                dayYes[d] += 1

    m = dayYes[0]
    for i in range(1, 5):
        if m < dayYes[i]:
            m = dayYes[i]

    res = ""
    for i in range(5):
        if m == dayYes[i]:
            if res == "":
                res += str(i + 1)
            else:
                res += "," + str(i + 1)

    print(res)
