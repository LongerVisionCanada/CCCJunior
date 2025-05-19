if __name__ == "__main__":
    previous = ""
    while True:
        instr = int(input())
        if instr == 99999:
            break
        else:
            firstDigit = instr // 10000
            secondDigit = (instr % 10000) // 1000
            sumOf2Digits = firstDigit + secondDigit
            if sumOf2Digits % 2 == 1:
                previous = "left "
                print(previous + str(instr % 1000))
            elif sumOf2Digits % 2 == 0 and sumOf2Digits != 0:
                previous = "right "
                print(previous + str(instr % 1000))
            else:  # sumOf2Digits == 0
                print(previous + str(instr % 1000))
