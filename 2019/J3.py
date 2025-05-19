if __name__ == "__main__":
    N = int(input())

    for _ in range(N):
        s = input()

        pivot = s[0]
        curr = s[0]
        count = 1

        oneline = ""
        for i in range(1, len(s)):
            curr = s[i]
            if pivot == curr:
                count += 1
            else:
                oneline += str(count) + " " + pivot + " "
                pivot = curr
                count = 1

        oneline += str(count) + " " + pivot
        print(oneline)
