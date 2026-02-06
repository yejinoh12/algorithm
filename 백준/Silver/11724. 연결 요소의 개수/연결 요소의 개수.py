import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

gp = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    gp[a].append(b)
    gp[b].append(a)

# print(gp)

ans = 0
q = deque()
visited = [False for i in range(N + 1)]
for i in range(1, N + 1):
    if not visited[i]:
        # print(i)
        ans += 1
        q.append(i)
        visited[i] = True

    while q:
        v = q.popleft()
        for w in gp[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = True

print(ans)
