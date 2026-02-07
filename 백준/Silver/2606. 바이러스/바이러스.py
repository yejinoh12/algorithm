import sys

sys.setrecursionlimit(1000)

N = int(input())
M = int(input())

gp = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    gp[a].append(b)
    gp[b].append(a)

visited = [False for i in range(N + 1)]


def dfs(v):
    visited[v] = True
    cnt = 1
    for w in gp[v]:
        if not visited[w]:
            # print(f"{w}번째 정점 방문")
            cnt += dfs(w)
    return cnt


print(dfs(1) - 1)
