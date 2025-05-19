def isVowel(c: str) -> bool:
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        return True

    return False


# "a" is a vowel, and its ASCII code 97
# "z"'s ASCII code: 97+26-1=122
def cloestVowel(c: str) -> str:
    ascii_c = ord(c)
    d = 1
    while d < 26:
        if ascii_c - d >= 97:
            if isVowel(chr(ascii_c - d)):
                return chr(ascii_c - d)
        if ascii_c + d <= 122:
            if isVowel(chr(ascii_c + d)):
                return chr(ascii_c + d)
        d += 1


def nextConsonant(c: str) -> str:
    if c == "z":
        return "z"

    d = 1
    while True:
        cn = chr(ord(c) + d)
        if not isVowel(cn):
            return cn
        else:
            d += 1


if __name__ == "__main__":
    word = input()

    out = ""

    for c in word:
        if isVowel(c):
            out += c
        else:
            out += c
            out += cloestVowel(c)
            out += nextConsonant(c)

    print(out)
