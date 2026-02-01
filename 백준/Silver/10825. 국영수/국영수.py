import sys
input = sys.stdin.readline

# 입력
# 이름, 국어, 영어 수학

# 정렬
# 국어 점수 감소 > 영어 점수 증가 > 수학 점수 감소 > 이름 사전 순
N = int(input())
arr = []
for _ in range(N):
    name, korean, english, math = input().split()
    korean = int(korean)
    english = int(english)
    math = int(math)
    arr.append([name, korean, english, math])

# print(arr)
arr.sort(key = lambda v : (-v[1], v[2], -v[3], v[0]))

for i in arr:
    sys.stdout.write(str(i[0]) + '\n')
