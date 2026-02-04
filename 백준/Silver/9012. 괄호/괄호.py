import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    v = input()
    cnt = 0
    flag = 0
    for i in range(len(v)):
        if '(' == v[i]:
            cnt += 1
        elif ')' == v[i]:
            cnt -= 1

        if cnt < 0:
            print("NO")
            flag = 1
            break

    if flag == 0:
        if cnt == 0:
            print("YES")
        else:
            print("NO")