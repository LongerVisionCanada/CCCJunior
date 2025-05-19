if __name__ == "__main__":
    P = int(input())
    C = int(input())

    if P > C:
        F = P * 50 - 10 * C + 500
    else:
        F = P * 50 - 10 * C

    print(F)
