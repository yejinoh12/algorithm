N = int(input())
tops = list(map(int, input().split()))

# print(tops)
stack = []
ans = []
for i in range(len(tops)):
    while stack and tops[i] >= stack[-1][0]:
        stack.pop()

    if not stack:
        ans.append(0)
    else:
        ans.append(stack[-1][1])

    stack.append([tops[i], i + 1])

print(*ans)