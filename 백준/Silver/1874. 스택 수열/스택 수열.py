import sys

input = sys.stdin.readline

N = int(input())
target = [int(input()) for _ in range(N)]

stack = []
ops = []
cur = 1

for v in target:
    while cur <= v:
        stack.append(cur)
        ops.append("+")
        cur += 1

    if stack[-1] != v:
        ops.clear()
        break
    else:
        stack.pop()
        ops.append("-")

if ops:
    for x in ops:
        print(x)
else:
    print("NO")