def DFS(S: int, I: str, F: str, rules: list[tuple], route: list[tuple]) -> list[tuple]:
    if S == 0 and I == F:
        return route
    if S <= 0:
        return None

    for r in range(3):
        rule = rules[r]
        if rule[0] in I:
            li = len(I)
            lr = len(rule[0])
            for i in range(li - lr + 1):
                if I[i : i + lr] == rule[0]:
                    tmp = I[0:i] + rule[1]
                    if i + lr < li:
                        tmp += I[i + lr :]
                    # tmpRoute = route is wrong!!
                    tmpRoute = list(route)
                    tmpRoute.append((r + 1, i + 1, tmp))
                    res = DFS(S - 1, tmp, F, rules, tmpRoute)
                    if res is not None:
                        return res

    return None


if __name__ == "__main__":
    rules = []
    for _ in range(3):
        x, y = input().split()
        rules.append((x, y))

    s, I, F = input().split()
    S = int(s)

    # 3^15=14348907

    route = []
    route = DFS(S, I, F, rules, route)
    for r in route:
        print(f"{r[0]} {r[1]} {r[2]}")
