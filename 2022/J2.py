if __name__ == "__main__":
    N = int(input())

    counter = 0
    for i in range(N):
        points = int(input())
        fouls = int(input())
        total = 5 * points - 3 * fouls
        if total > 40:
            counter += 1

    if counter == N:
        print(str(counter) + "+")
    else:
        print(counter)
