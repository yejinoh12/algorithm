import sys

input = sys.stdin.readline
out = sys.stdout.write

n = int(input())
numbers = [int(input()) for _ in range(n)]

numbers.sort()

out('\n'.join(map(str, numbers)))