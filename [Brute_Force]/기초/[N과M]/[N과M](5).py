# N과M 5 # B_15654
# (1)과 대응되는 문제
# 하지만 1부터 'N까지의 수'가 아닌 'N개의 서로 다른 자연수'
import sys
n, m = map(int, input().split())
num = list(map(int, input().split())) # [(1)과 다른 부분]
num.sort()  # 사전 순 정렬[(1)과 다른 부분]
check = [False]*n
a = [0]*m  # 정답을 넣는 배열


def nm(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a))+'\n')
        return
    for i in range(n):
        # 중복 불가. 즉, 해당 수를 사용했다면 넘어가야함
        if check[i]:
            continue
        check[i] = True  # 사용했으면 True
        a[index] = num[i]  # 입력으로 받은 수 최소 순으로 넣기[(1)과 다른 부분]
        nm(index+1, n, m)  # 다음 위치 찾기
        check[i] = False # 한 패턴을 돌고 나면 초기화


nm(0, n, m)