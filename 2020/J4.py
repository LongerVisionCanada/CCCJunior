def isCyclicShift(s1: str, s2: str) -> bool:
    # len(s1) == len(s2)
    l = len(s1)
    for i in range(l):
        cs = s1[i:] + s1[0:i]
        if cs == s2:
            return True

    return False


if __name__ == "__main__":
    T = input()
    S = input()

    lt = len(T)
    ls = len(S)

    res = "no"
    if lt >= ls:
        # ABCCDEABAA
        # ABCDE
        for i in range(lt - ls + 1):
            if isCyclicShift(T[i : i + ls], S):
                res = "yes"
                break

    print(res)
