if __name__ == "__main__":
    N = int(input())
    k = int(input())

    sum = N
    for i in range(k):
        N *= 10
        sum += N

    print(sum)
