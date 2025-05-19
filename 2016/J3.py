def isPalindrome(s: str) -> bool:
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[l - i - 1]:
            return False

    return True


if __name__ == "__main__":
    line = input()
    l = len(line)

    lpl = l

    found = False
    while lpl > 1 and not found:
        for i in range(l - lpl + 1):
            tmp = line[i : i + lpl]
            if isPalindrome(tmp):
                found = True
                break

        if not found:
            lpl -= 1

    print(lpl)
