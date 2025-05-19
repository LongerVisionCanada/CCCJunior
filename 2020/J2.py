if __name__ == "__main__":
    P = int(input())
    N = int(input())
    R = int(input())

    day = 0
    infectedOnTheDay = N
    total = N

    while total <= P:
        day += 1
        infectedOnTheDay *= R
        total += infectedOnTheDay

    print(day)
