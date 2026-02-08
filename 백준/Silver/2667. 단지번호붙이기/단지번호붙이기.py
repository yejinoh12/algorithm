from collections import deque

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip())))

cnt = 0  # 단지수(BFS 함수가 실행된 횟수)
ans = []  # 각 단지내 집의 수: 큐 방문 횟수


def bfs(x, y):
    global cnt
    cnt += 1
    house = 1
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
                house += 1

    return house


for i in range(N):
    for j in range(N):
        # print(f'(y={i},x={j})')
        # print(arr[i][j])
        if arr[i][j] == 1:
            ans.append(bfs(j, i))
        else:
            pass

ans.sort()
print(cnt)
print('\n'.join(map(str, ans)))
