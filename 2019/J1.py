if __name__ == "__main__":
    A3 = int(input())
    A2 = int(input())
    A1 = int(input())

    B3 = int(input())
    B2 = int(input())
    B1 = int(input())

    AS = A3 * 3 + A2 * 2 + A1 * 1
    BS = B3 * 3 + B2 * 2 + B1 * 1

    if AS > BS:
        print("A")
    elif BS > AS:
        print("B")
    else:
        print("T")
