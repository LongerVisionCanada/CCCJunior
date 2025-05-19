if __name__ == "__main__":
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    t = int(input())

    dist = abs(c - a) + abs(d - b)
    if t < dist:
        print("N")
    else:
        if (t - dist) % 2 == 0:
            print("Y")
        else:
            print("N")
