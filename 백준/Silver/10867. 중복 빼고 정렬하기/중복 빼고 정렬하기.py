import sys
input = sys.stdin.readline

N = int(input())

numbers = set(map(int, input().split()))
print(*sorted(numbers))