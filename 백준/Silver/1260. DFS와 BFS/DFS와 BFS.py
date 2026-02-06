import sys
from collections import deque

sys.setrecursionlimit(10000)

N, M, V = map(int, input().split())

gp = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    gp[a].append(b)
    gp[b].append(a)

for i in gp:
    i.sort()


def bfs(v):
    q = deque([v])
    visit[v] = 1
    print(v, end=' ')
    while q:
        v = q.popleft()
        for w in gp[v]:
            if visit[w] == 0:
                q.append(w)
                visit[w] = 1
                print(w, end=' ')


def dfs(v):
    visit[v] = 1
    print(v, end=' ')
    for w in gp[v]:
        if visit[w] == 0:
            dfs(w)


visit = [0 for i in range(N + 1)]
dfs(V)
print()
visit = [0 for i in range(N + 1)]
bfs(V)
