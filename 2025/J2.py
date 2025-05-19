if __name__ == "__main__":
    D = int(input())
    E = int(input())
    R = D
    for i in range(E):
        s = input()
        if s=='+':
            R += int(input())
        else:
            R -= int(input())
    
    print(R)
