# 두 배열의 합 # B_2143
# 부분수열의 합2 와 같은 문제
# 부분수의 합2 # B_1208
# 중간에서 만나기 / 교안참고
# N개가 있다고 할 때 M=2/N개 N-M개로 나누어 계산하여 시간복잡도를 줄임
from collections import Counter

goal = int(input())

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

first, second = [], []

# first, second: a 와 b 각 수열의 합으로 나타낼 수 있는 부분 집합들
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += a[j]
        first.append(sum)
for i in range(m):
    sum = 0
    for j in range(i,m):
        sum += b[j]
        second.append(sum)

first.sort()
second.sort()
c = Counter(second)
ans = 0

for num in first:
    """
    (c[goal-num])? : goal-fisrt요소 = 필요한 second요소
    # goal:5 , fisrt = [1,1,2,3,3,4,4]라면
    # 5-1 = 4이므로 5가되기 위한 4가 second 리스트에 몇개 있는지 조사
    """
    ans += c[goal-num]
print(ans)