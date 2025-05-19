if __name__ == "__main__":
    S = int(input())
    M = int(input())
    L = int(input())

    score = 1 * S + 2 * M + 3 * L

    if score >= 10:
        print("happy")
    else:
        print("sad")
