import sys

input = sys.stdin.readline

n = int(input())

count_arr = [0] * 10001
for _ in range(n):
    num = int(input())
    count_arr[num] += 1

for i in range(len(count_arr)):
    for _ in range(count_arr[i]):
        sys.stdout.write(str(i) + '\n')