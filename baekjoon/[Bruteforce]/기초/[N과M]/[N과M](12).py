# N과M 12  B_15665
# 중복 선택 가능, 비내림차순
# 다른점: 입력받는 수에 같은 수가 있을 수 있음 제거하고 시작

import sys
n, m = map(int, input().split())
num = list(set(map(int, input().split()))) # [(1)과 다른 부분]
num.sort()  # 사전 순 정렬[(1)과 다른 부분]
check = [False]*n
n = len(num)  # 중복된 수 제거 되어 입력된 수가 줄어들 수 있기 때문
a = [0]*m  # 정답을 넣는 배열

def solution(index, start, n, m):
    if index == m:
        for i in range(m):
            sys.stdout.write(str(num[a[i]])+' ')
        sys.stdout.write('\n')
        return
    for i in range(start, n):
        check[i] = True
        a[index] = i
        solution(index+1, i, n, m)
        check[i] = False

solution(0, 0, n, m)
