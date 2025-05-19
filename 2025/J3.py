if __name__ == "__main__":
    N = int(input())
    
    for i in range(N):
        s = input()
        
        uppers = ''
        sum = 0
        num = ''
        for c in s:
            if c.isupper():
                uppers += c
                if num != '':
                    sum += int(num)
                    num = ''
            elif c.islower():
                if num != '':
                    sum += int(num)
                    num = ''
            elif c == '-':
                if num != '':
                    sum += int(num)
                num = '-'
            elif c.isdigit():
                num += c
        
        if num != '':
            sum += int(num)
        
        print(uppers + str(sum))