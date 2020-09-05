# 퍼즐 # B_1525
# 복잡해서 그냥 넘어가도 되는 문제
"""
# 정점은 최대 9!개 = 362,880개
# 처음 0 의 위치를 출발점으로보고 항상 정렬이 된 후에는 0이 제일 마지막에 있으므로
# 최단거리 문제로 보고 풀이
"""
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = 3
a = [list(map(int,input().split())) for _ in range(n)]
start = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            a[i][j] = 9
        start = start * 10 + a[i][j]  # 3x3행렬을 한줄의 숫자로 저장
        # ex) 1 0 3
        #     4 2 5
        #     7 8 6   -> 103425786
q = deque()
dist = dict()  # dictionary 선언
dist[start] = 0
q.append(start)
while q:
    now_num = q.popleft()
    now = str(now_num)  # 수를 문자열로 바꿈
    z = now.find('9')  # 9의 위치
    x = z//3  # '9'의 세로(행) 좌표
    y = z%3  # '9'의 가로(열) 좌표
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            temp = list(now)
            temp[x*3+y],temp[nx*3+ny] = temp[nx*3+ny],temp[x*3+y]
            num = int(''.join(temp))  # 인덱싱을 위해 문자열을 다시 수로 바꿈
            if num not in dist:
                dist[num] = dist[now_num] + 1  # 지금까지의 해당 수의 연산 횟수 +1
                q.append(num)

if 123456789 in dist:
    print(dist[123456789])  # 123456789가 된게 있다면 연산횟수 출력
else:
    print(-1)

