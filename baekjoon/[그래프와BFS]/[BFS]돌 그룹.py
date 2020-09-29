# 돌 그룹 # B_12886
"""
# BFS로 해결할 수 있다. 여기서는 DFS로 풀이
# BFS로는 몇번만에 가능한지까지 구할 수 있음
# 정점: (A,B,C) 또는 (A,B)
# 전제 정점의 개수: A+B+C

***키포인트***
1500^3은 크기가 너무 큼 그래서 A,B만 사용 1500^2으로 풀이
그럼 C는 어떻게 구함? 모든 돌그룹은 새로운 수가 추가되는것이 아니므로 전체 갯수에서 두가지를 빼는 방법으로
C를 구할 수 있음
***********

"""
# DFS
import sys
sys.setrecursionlimit(1500*1500)
check = [[False]*1501 for _ in range(1501)]
x, y, z = map(int, input().split())  # 돌 갯수 입력
s = x+y+z  # 돌의 총 갯수


def go(x,y):
    if check[x][y]:  # 이미 해 본 경우이면 pass
        return

    check[x][y] = True
    a = [x, y, s-x-y]  # 그룹 A,B,C
    # 대소 관계를 통해 해결
    for i in range(3):
        for j in range(3):
            if a[i] < a[j]:
                b = [x, y, s-x-y]
                b[i] += a[i]
                b[j] -= a[i]
                go(b[0], b[1])


# 돌의 총 갯수가 3으로 나누어떨어져야 3등분 균일 분배 가능
if s % 3 != 0:  # 3으로 나누어 떨어지지 않으면 0 출력
    print(0)
else:  # 나누어 떨어진다면 본격 풀이 시작
    go(x, y)
    if check[s//3][s//3]:  # 3등분 된 경우가 True면 1 출력
        print(1)
    else:
        print(0)
