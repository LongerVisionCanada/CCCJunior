if __name__ == "__main__":
    M = int(input())

    t = 0
    d = {}
    for _ in range(M):
        comm, x = input().split()
        X = int(x)
        if comm == "W":
            t += X - 1
        else:
            if X not in d:
                d[X] = [(comm, t)]
            else:
                d[X].append((comm, t))
            t += 1

    dkey = sorted(d)
    for person in dkey:
        l = len(d[person])
        if l % 2 == 1:
            print(str(person) + " " + str(-1))
        else:
            tt = 0
            for i in range(l):
                if i % 2 == 0:
                    tt -= d[person][i][1]
                else:
                    tt += d[person][i][1]

            print(str(person) + " " + str(tt))
