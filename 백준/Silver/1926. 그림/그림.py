"""
그림의 개수와 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력
"""
import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def dfs(x, y):
    arr[y][x] = 0  # 방문 처리
    size = 1  # 현재 칸의 넓이

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1:
            size += dfs(nx, ny)

    return size


count = 0
max_area = 0
for y in range(n):
    for x in range(m):
        if arr[y][x] == 1:
            # print(f"호출 좌표: {x, y}")
            count += 1
            area = dfs(x, y)
            max_area = max(area, max_area)

print(count)
print(max_area)
