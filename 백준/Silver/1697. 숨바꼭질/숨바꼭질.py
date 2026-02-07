from collections import deque

N, K = map(int, input().split())

MAX = 100_000
dist = [-1] * (MAX + 1)

q = deque([N])
dist[N] = 0

while q:
    v = q.popleft()
    # print("큐에서 꺼낸거", v)

    if v == K:
        print(dist[v])
        break

    for w in [v * 2, v + 1, v - 1]:
        # print("인접 노드 검사", w)
        if 0 <= w <= MAX and dist[w] == -1:
            dist[w] = dist[v] + 1
            q.append(w)
