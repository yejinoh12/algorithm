import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    J, N = input().split()
    J = int(J)
    N = int(N)

    arr = []
    for _ in range(N):
        r, c = input().split()
        r = int(r)
        c = int(c)
        arr.append([r, c])

    # print(arr)

    arr.sort(key = lambda v : v[0] * v[1], reverse=True)
    # print(arr)

    cnt = 0
    for v in arr:
        J = J - (v[0] * v[1])
        cnt += 1
        # print(J)
        if J <= 0:
            break

    print(cnt)