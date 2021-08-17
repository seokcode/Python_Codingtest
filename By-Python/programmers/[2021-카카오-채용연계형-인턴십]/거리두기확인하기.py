import collections

def solution(places):
    answer = []   
    
    for p in places:
        answer.append(bfs(p))
            
    return answer

def bfs(place):
    # 우, 하, 좌, 상
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    # 응시자 위치 파악
    # 5 * 5 고정이기 때문에 시간이 크게 다르지 않을 것이라 생각하여 그냥 한번에 응시자 위치를 다 구해놓고 시작
    people = []
    for i in range(len(place)):
        for j in range(len(place[0])):
            if place[i][j] == "P":
                people.append([i,j])
    
    for (px,py) in people:    
        visited = [[False for _ in range(5)] for _ in range(5) ]
        dq = collections.deque()
        
        visited[px][py] = True
        dq.append([px,py,0])
    
        while dq:
            x,y,cost = dq.popleft()

            # 한명이라도 어겼다면 0 return
            # 사람 간의 거리가 2이하인 경우 -> 무조건 방역수칙 위반
            if 1 <= cost <= 2 and place[x][y] == "P":
                return 0
            # 거리가 3 이상이라면 -> 무조건 방역수칙 준수
            elif cost >= 3:
                break

            for direction in range(4):
                nx = [0,0,0]
                nx[0] += x + dx[direction]
                nx[1] += y + dy[direction]
                nx[2] += cost + 1

                if 0 <= nx[0] < 5 and 0 <= nx[1] < 5:
                    # 'X'(책상 = 벽)라서 더 나아가지 못하거나 이미 방문한 곳이 아니라면 dq에 추가
                    if place[nx[0]][nx[1]] != "X" and not visited[nx[0]][nx[1]]:
                        dq.append(nx)
                        visited[nx[0]][nx[1]] = True
    # 모두 다 지켰다면 1 return
    return 1