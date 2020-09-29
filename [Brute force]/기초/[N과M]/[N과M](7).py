# N과M 7 # B_15656
# (3)과 대응 # (5)에서 중복 허용

import sys
n, m = map(int, input().split())
num = list(map(int, input().split())) # [(1)과 다른 부분]
num.sort()  # 사전 순 정렬[(1)과 다른 부분]
a = [0]*m  # 정답을 넣는 배열


def nm7(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a))+'\n')
        return
    for i in range(n):
        # 중복 불가. 즉, 해당 수를 사용했다면 넘어가야함
        a[index] = num[i]  # 입력으로 받은 수 최소 순으로 넣기[(1)과 다른 부분]
        nm7(index+1, n, m)  # 다음 위치 찾기


nm7(0, n, m)