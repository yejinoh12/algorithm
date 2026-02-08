from collections import deque

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip())))


def bfs(x, y):
    cnt = 1
    q = deque([(x, y)])
    arr[y][x] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if arr[ny][nx] == 1:
                q.append((nx, ny))
                arr[ny][nx] = 0
                cnt += 1
    return cnt


ans = []
for y in range(N):
    for x in range(N):
        if arr[y][x] == 1:
            ans.append(bfs(x, y))

ans.sort()
print(len(ans))
print('\n'.join(map(str, ans)))
