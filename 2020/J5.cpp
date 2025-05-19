#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

const int MAX_CELL = 1'000'001;
bool visited[MAX_CELL];

// 深度优先搜索函数
bool DFS(unordered_map<int, vector<int>> &v2c, int cell, int M, int N)
{
    if (cell == M * N)
        return true;
    if (v2c.find(cell) == v2c.end())
        return false;
    if (visited[cell])
        return false;

    visited[cell] = true;

    for (int next : v2c[cell])
    {
        if (!visited[next] && DFS(v2c, next, M, N))
        {
            return true;
        }
    }

    return false;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N;
    cin >> M >> N;

    unordered_map<int, vector<int>> v2c;
    for (int m = 0; m < M; ++m)
    {
        for (int n = 0; n < N; ++n)
        {
            int x;
            cin >> x;
            int key = (m + 1) * (n + 1);
            v2c[key].push_back(x);
        }
    }

    fill(begin(visited), end(visited), false);
    int start = v2c.count(1) ? v2c[1][0] : -1;

    if (start != -1 && DFS(v2c, start, M, N))
    {
        cout << "yes\n";
    }
    else
    {
        cout << "no\n";
    }

    return 0;
}
