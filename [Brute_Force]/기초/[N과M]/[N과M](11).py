# N과M 11  B_15665
# 중복 선택 가능
# 다른점: 입력받는 수에 같은 수가 있을 수 있음 제거하고 시작

import sys
from collections import Counter
n, m = map(int, input().split())
# set을 이용하여 중복되는 수 제거
num = list(set((map(int, input().split()))))
num.sort()
n = len(num)
check = [False]*n
a = [0]*m  # 정답을 넣는 배열

def solution(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(n):
        check[i] = True
        a[index] = num[i]
        solution(index+1, n, m)
        check[i] = False

solution(0,n,m)
