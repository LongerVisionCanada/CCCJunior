if __name__ == "__main__":
    q = int(input())
    N = int(input())

    D = list(map(int, input().split()))
    P = list(map(int, input().split()))

    # a is from D, b is from P
    # bicyle speed is determined by max(a,b)

    if q == 1:
        D.sort()
        P.sort()
        s = 0
        for i in range(N):
            s += max(D[i], P[i])
        print(s)
    else:  # q==2
        A = D + P  # len(A) must be 2*N
        A.sort(reverse=True)
        s = 0
        for i in range(N):
            s += A[i]
        print(s)
