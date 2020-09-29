# N과M 6 # B_15655
# (2)와 대응 # (5) 에서 오름차순 조건만 추가됨

import sys
n, m = map(int, input().split())
num = list(map(int, input().split())) # [(1)과 다른 부분]
num.sort()  # 사전 순 정렬[(1)과 다른 부분]
check = [False]*n
a = [0]*m  # 정답을 넣는 배열

# 방법 1
def nm6(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a))+'\n')
        return
    for i in range(start, n):
        # 중복 불가. 즉, 해당 수를 사용했다면 넘어가야함
        if check[i]:
            continue
        check[i] = True  # 사용했으면 True
        a[index] = num[i]  # 입력으로 받은 수 최소 순으로 넣기[(1)과 다른 부분]
        nm6(index+1, i+1, n, m)  # 다음 위치 찾기
        check[i] = False # 한 패턴을 돌고 나면 초기화


# (2)는 1,2,3,4~ 이런식이라서 인자값에 1을 넣었지만 (6)은 입력된 수를
# 가지고 하기 때문에 start도 0부터 시작
nm6(0, 0, n, m)


# 방법 2
def nm6_2(index, selected, n, m):
    if selected == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    if index >= n:
        return
    a[selected] = num[index]
    nm6_2(index+1, selected+1, n, m)
    a[selected] = 0
    nm6_2(index+1, selected, n, m)

nm6_2(0,0,n,m)


