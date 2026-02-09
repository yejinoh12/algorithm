from collections import deque

T = int(input())


def bfs(x, y, arr, w, h):
    q = deque()
    q.append((x, y))
    arr[y][x] = 0
    while q:
        cx, cy = q.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue

            if arr[ny][nx] == 1:
                q.append((nx, ny))
                arr[ny][nx] = 0


def solve():
    w, h, k = map(int, input().split())
    gp = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(k):
        x, y = map(int, input().split())
        gp[y][x] = 1

    ans = 0
    for y in range(h):
        for x in range(w):
            if gp[y][x] == 1:
                ans += 1
                bfs(x, y, gp, w, h)

    print(ans)

for _ in range(T):
    solve()