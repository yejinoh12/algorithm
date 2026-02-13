from collections import deque

n, m = map(int, input().split())

arr = []
for i in range(n):
    v = list(map(int, input()))
    arr.append(v)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y, 1))
    arr[y][x] = 0
    while q:
        cx, cy, dist = q.popleft()

        if cx == m - 1 and cy == n - 1:
            print(dist)
            return

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1:
                q.append((nx, ny, dist + 1))
                arr[ny][nx] = 0


bfs(0, 0)
