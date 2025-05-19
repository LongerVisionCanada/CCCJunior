if __name__ == "__main__":
    N = int(input())

    highestName = ""
    highestBid = -1

    for i in range(N):
        name = input()
        score = int(input())
        if score > highestBid:
            highestBid = score
            highestName = name

    print(highestName)
