# 합이 0인 네 정수 # B_7453
# N제한이 길어서 그냥 다 구하기엔 시간 복잡도 O(N^4)
# 중간에서 만나기로 풀이 / 부분수열의 합2, 두 배열의 합과 비슷
"""
이분탐색사용 함수(교안 참고)
# lower bound: 찾으려는 수보다 크거나 같으면서 가장 작은 수
# upper bound: 찾으려는 수보다 크면서 가장 작은 수
# upper bound - lower bound 를 해주면 찾으려는 수의 갯수를 찾을 수 있음

def upper_bound(a, val):
    left = 0
    right = len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] <= val:
            left = mid+1
        else:
            right = mid
    return left

def lower_bound(a, val):
    left = 0
    right = len(a)
    while left < right:
        mid = (left + right) / 2
        if a[mid] >= val:
            right = mid
        else:
            left = mid+1
    return left
"""

import sys
from collections import Counter

n = int(sys.stdin.readline())
temp = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a,b,c,d = zip(*temp)
# print(a,b,c,d)
first = []
second = []

for i in range(n):
    for j in range(n):
        first.append(a[i]+b[j])
        second.append(c[i]+d[j])

counter = Counter(second)
ans = 0
for num in first:
    # A[a]+B[b]+C[c]+D[d] = 0
    # A[a]+B[b] = -(C[c]+D[d])
    ans += counter[-num]  # goal(0)-num
print(ans)

