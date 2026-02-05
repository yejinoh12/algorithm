N = int(input())

arr = []
for _ in range(N):
    s = input().strip()
    arr.append(s)

s = set(arr)
arr = list(s)

arr.sort(key=lambda v: (len(v), v))

for i in arr:
    print(i)