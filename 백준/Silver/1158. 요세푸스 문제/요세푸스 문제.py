from collections import deque

K, N = map(int, input().split())

q = deque()
for i in range(1, K + 1):
    q.append(i)

i = 1
arr = []
while q:
    if i % N == 0:
        arr.append(q.popleft())
    else:
        q.append(q.popleft())
    i += 1

    if not q:
        break

print("<", end="")
for i in range(len(arr)):
    if i == len(arr) - 1:
        print(arr[i], end='')
    else:
        print(arr[i], end=', ')
print(">")
