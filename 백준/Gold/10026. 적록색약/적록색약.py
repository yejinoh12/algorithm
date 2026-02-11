from collections import deque
import copy
n = int(input())

arr = []
arr_ = []
for i in range(n):
    row = list(map(str, input()))
    arr.append(row)
    row_= [x if x != 'G' else 'R' for x in row]
    arr_.append(row_)

def bfs(x, y, gp):
    # print("BFS 실행 좌표: ", x, y)
    q = deque()
    q.append((x, y, gp[y][x]))
    gp[y][x] = 'V'
    while q:
        cx, cy, cs = q.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for w in range(4):
            nx = cx + dx[w]
            ny = cy + dy[w]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if gp[ny][nx] != 'V' and cs == gp[ny][nx]:
                # print("큐 삽입: ", nx, ny)
                q.append((nx, ny, gp[ny][nx]))
                gp[ny][nx] = 'V'


# print(arr)
# print(arr_)

ans = 0
ans_ = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != 'V':
            ans += 1
            bfs(j, i, arr)
        if arr_[i][j] != 'V':
            ans_ += 1
            bfs(j, i, arr_)

print(ans, ans_)
