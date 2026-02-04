T = int(input())

for _ in range(T):
    s = input().strip()

    left = []  # 커서의 왼쪽 문자들
    right = []  # 커서의 오른쪽 문자들

    for ch in s:
        if ch == '<':
            if left:
                right.append(left.pop())
        elif ch == '>':
            if right:
                left.append(right.pop())
        elif ch == '-':
            if left:
                left.pop()
        else:
            left.append(ch)


    left.extend(reversed(right))
    print("".join(left))