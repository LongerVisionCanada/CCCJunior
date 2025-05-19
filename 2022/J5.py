if __name__ == "__main__":
    N = int(input())
    T = int(input())

    trees = []
    for i in range(T):
        R, C = input().split()
        trees.append(((int)(R), (int)(C)))

    # Largest square of 0s in a 2D sparse binary matrix
    # - recursion + historical record
    # - DP

    M = 1
    # limits
    sortedTreesByRow = sorted(trees, key=lambda x: (x[0], x[1]))
    sortedTreesByCol = sorted(trees, key=lambda x: (x[1], x[0]))
    sortedRows = [0] + sorted(list(set(x[0] for x in sortedTreesByRow))) + [N + 1]
    # print(sortedRows)

    for r1Idx in range(len(sortedRows) - 1):
        for r2Idx in range(r1Idx + 1, len(sortedRows)):
            tmpM = sortedRows[r2Idx] - sortedRows[r1Idx] - 1
            if tmpM > M:
                filteredTrees = [
                    (x[0], x[1])
                    for x in sortedTreesByCol
                    if sortedRows[r1Idx] < x[0] < sortedRows[r2Idx]
                ]
                sortedColsBetweenRows = (
                    [0] + sorted(list(set(x[1] for x in filteredTrees))) + [N + 1]
                )
                # print(sortedColsBetweenRows)
                diffs = [
                    sortedColsBetweenRows[i + 1] - sortedColsBetweenRows[i] - 1
                    for i in range(len(sortedColsBetweenRows) - 1)
                ]
                if max(diffs) >= tmpM:
                    M = tmpM

    sortedCols = [0] + sorted(list(set(x[1] for x in sortedTreesByCol))) + [N + 1]

    for r1Idx in range(len(sortedCols) - 1):
        for r2Idx in range(r1Idx + 1, len(sortedCols)):
            tmpM = sortedCols[r2Idx] - sortedCols[r1Idx] - 1
            if tmpM > M:
                filteredTrees = [
                    (x[0], x[1])
                    for x in sortedTreesByRow
                    if sortedCols[r1Idx] < x[1] < sortedCols[r2Idx]
                ]
                sortedRowsBetweenCols = (
                    [0] + sorted(list(set(x[0] for x in filteredTrees))) + [N + 1]
                )
                # print(sortedColsBetweenRows)
                diffs = [
                    sortedRowsBetweenCols[i + 1] - sortedRowsBetweenCols[i] - 1
                    for i in range(len(sortedRowsBetweenCols) - 1)
                ]
                if max(diffs) >= tmpM:
                    M = tmpM

    print(M)
