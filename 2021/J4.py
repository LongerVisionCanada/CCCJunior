if __name__ == "__main__":
    books = input()

    nbOfLs = 0
    nbOfMs = 0
    nbOfSs = 0

    for c in books:
        if c == "L":
            nbOfLs += 1
        elif c == "M":
            nbOfMs += 1
        else:  # c == "S"
            nbOfSs += 1

    # all locations in the left most nbOfLs
    # should be L but now not L, are going to
    # be swapped out
    LAtL = 0
    MAtL = 0
    SAtL = 0
    for i in range(nbOfLs):
        if books[i] == "L":
            LAtL += 1
        elif books[i] == "M":
            MAtL += 1
        else:
            SAtL += 1

    LAtM = 0
    MAtM = 0
    SAtM = 0
    for i in range(nbOfMs):
        if books[nbOfLs + i] == "L":
            LAtM += 1
        elif books[nbOfLs + i] == "M":
            MAtM += 1
        else:
            SAtM += 1

    LAtS = 0
    MAtS = 0
    SAtS = 0
    for i in range(nbOfSs):
        if books[nbOfLs + nbOfMs + i] == "L":
            LAtS += 1
        elif books[nbOfLs + nbOfMs + i] == "M":
            MAtS += 1
        else:
            SAtS += 1

    nbOfSwaps = 0
    if LAtS <= SAtL:
        # nbOfSwaps += LAtS
        nbOfSwaps += LAtM
        nbOfSwaps += SAtM
        # nbOfSwaps += SAtL - LAtS
        nbOfSwaps += SAtL
    else:
        # nbOfSwaps += SAtL
        nbOfSwaps += LAtM
        nbOfSwaps += SAtM
        # nbOfSwaps += LAtS - SAtL
        nbOfSwaps += LAtS

    print(nbOfSwaps)
