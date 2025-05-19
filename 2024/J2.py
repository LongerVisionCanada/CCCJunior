if __name__ == "__main__":
    D = int(input())
    R = D

    while True:
        Y = int(input())
        if R > Y:
            R += Y
        else:
            break

    print(R)
