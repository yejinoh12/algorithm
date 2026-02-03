import sys

input = sys.stdin.readline

N = int(input())
target = [int(input()) for _ in range(N)]

stack = []
ops = []
cur = 1 # 다음에 푸시 할 수 있는 가장 작은 숫자

for i in range(len(target)):
    v = target[i]
    # print(f"===============현재 꺼내야하는 숫자: {v}=====================")
    # 스택이 비지 않고
    if stack:
        if stack[-1] > target[i]:
            ops.clear()
            break
        elif stack[-1] == v:
            stack.pop()
            ops.append("-")
            # print(">> 숫자 발견 팝 완료")
            # print(">> 현재 스택", stack)
            continue

    while cur <= v:
        stack.append(cur)
        ops.append("+")
        cur += 1
        # print(">>현재 스택", stack)
        # print(">>현재 숫자:", cur)

    stack.pop()
    ops.append("-")
    # print(f">>특정 숫자 {v} 까지 모두 넣고 팝 완료")
    # print(">>현재 스택", stack)
    # print(f"===============완료=====================")

if ops:
    for v in ops:
        print(v)
else:
    print("NO")