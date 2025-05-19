if __name__ == "__main__":
    m = int(input())
    d = int(input())

    if m == 2 and d == 18:
        print("Special")
    elif m == 1 or (m == 2 and d < 18):
        print("Before")
    else:
        print("After")
