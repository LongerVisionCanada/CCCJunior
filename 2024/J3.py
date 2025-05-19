if __name__ == "__main__":
    N = int(input())

    scores = []
    for i in range(N):
        scores.append(int(input()))

    scores = sorted(scores, reverse=True)
    s = sorted(set(scores), reverse=True)

    counter = 0
    for sc in scores:
        if sc == s[2]:
            counter += 1
        elif sc < s[2]:
            break

    print(f"{s[2]} {counter}")
