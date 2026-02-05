from collections import deque

K, N = map(int, input().split())
q = deque(range(1, K + 1))
ans = []

while q:
    q.rotate(-(N - 1))
    ans.append(q.popleft())

print("<" + ", ".join(map(str, ans)) + ">")