s = input().strip()

stack = []
cnt = 0
ans = 0
for i in range(len(s)):
    if s[i] in '(':
        stack.append(s[i])
        cnt += 1
        pass
    elif s[i] in ')':
        if stack:
            if s[i - 1] == '(':
                stack.pop()
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1
        else:
            break

print(ans)