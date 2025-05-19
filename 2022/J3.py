if __name__ == "__main__":
    s = input()

    harpStrings = ""
    numStr = ""
    numStart = False
    for c in s:
        if c.isupper():
            if numStart:
                numStart = False
                harpStrings += " " + numStr
                print(harpStrings)
                harpStrings = ""
                numStr = ""
            harpStrings += c
        elif c == "+":
            harpStrings += " tighten"
        elif c == "-":
            harpStrings += " loosen"
        else:  # 0~9
            numStart = True
            numStr += c

    print(harpStrings + " " + numStr)
