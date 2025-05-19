import queue


if __name__ == "__main__":
    N = int(input())

    M = {0: 0}
    for i in range(N):
        row = list(map(int, input().split()))
        if i + 1 not in M:
            M[i + 1] = row[1:]

    visited = [False] * (N + 1)  # ignore visited[0]
    q = queue.Queue()
    q.put((1, 1))

    K = 10002
    while not q.empty():
        tpl = q.get()
        page = tpl[0]
        step = tpl[1]
        if not visited[page]:
            visited[page] = True
            if len(M[page]) == 0:
                if step < K:
                    K = step
            for m in M[page]:
                if not visited[m]:
                    q.put((m, step + 1))

    line1 = "Y"
    for i in range(1, N + 1):
        if not visited[i]:
            line1 = "N"
            break

    print(line1)
    print(K)
