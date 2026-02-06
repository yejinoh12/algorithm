import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
gp = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    gp[a].append(b)
    gp[b].append(a)

ans = 0
visited = [False for i in range(N + 1)]


def dfs(v):
    visited[v] = True
    for w in gp[v]:
        if not visited[w]:
            dfs(w)


for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)
