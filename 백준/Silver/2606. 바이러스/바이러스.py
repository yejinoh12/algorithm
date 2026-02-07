from collections import deque

N = int(input())
M = int(input())

gp = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    gp[a].append(b)
    gp[b].append(a)

visited = [False for i in range(N + 1)]
q = deque([1])
visited[1] = True

ans = 0
while q:
    v = q.popleft()
    for w in gp[v]:
        if not visited[w]:
            q.append(w)
            visited[w] = True
            ans += 1

print(ans)
