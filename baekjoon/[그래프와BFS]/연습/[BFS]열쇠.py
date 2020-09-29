# 열쇠 # B_9328

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = ['*.'+input()+'.*' for _ in range(n)]
    print(a)
    n += 4
    m += 4
    # 상근이는 처음에는 빌딩의 밖에 있으며,
    # 빌딩 가장자리의 빈 공간이나 문을 통해 빌딩 안팎을 드나들 수 있다.
    a = ['*'*m,'*'+'.'*(m-2)+'*'] + a + ['*'+'.'*(m-2)+'*','*'*m]
    print(a)
    key = set(input())
    ans = 0
    check = [[False]*m for _ in range(n)]
    q = deque()
    door = [deque() for _ in range(26)]
    q.append((1,1))
    check[1][1] = True
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if check[nx][ny]:
                continue
            w = a[nx][ny]
            if w == '*':
                continue
            check[nx][ny] = True
            if w == '.':
                q.append((nx,ny))
            elif w == '$':  # 문서를 발견하면
                q.append((nx,ny))
                ans += 1  # 답 +1
            elif 'A' <= w <= 'Z':  # 문을 만났을 때
                # lower(): 소문자로 바꾸는 메소드
                if w.lower() in key:  # 그 문의 열쇠를 가지고 있다면 q에 저장
                    q.append((nx,ny))
                else:  # 없다면 해당 문 앞에서 대기, door에 현재 위치 저장
                    door[ord(w)-ord('A')].append((nx,ny))
            elif 'a' <= w <= 'z':  # 열쇠를 얻었을 때 방문은 하는
                q.append((nx,ny))
                if not w in key:  # 키가 없었다면
                    key.add(w)  # 키를 얻었다고 표시
                    # append는 x 그 자체를 원소로 넣고 extend는 iterable의 각 항목들을 넣습니다
                    q.extend(door[ord(w)-ord('a')])  # 문 앞에서 대기하는 사람 넣어
    print(ans)

"""
# 상근이는 처음에는 빌딩의 밖에 있으며,
# 빌딩 가장자리의 빈 공간이나 문을 통해 빌딩 안팎을 드나들 수 있다.
1)
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*

2) a = ['*.'+input()+'.*' for _ in range(n)]?
*.*****************.*
*..............**$*.*
*.*B*A*P*C**X*Y*.X..*
*.*y*x*a*p**$*$**$*.*
*.*****************.*

3) a = ['*'*m,'*'+'.'*(m-2)+'*'] + a + ['*'+'.'*(m-2)+'*','*'*m]
*********************   
*...................*   # 건물 밖 통로
*.*****************.*   # 여기부터
*..............**$*.*   # ~
*.*B*A*P*C**X*Y*.X..*   # ~
*.*y*x*a*p**$*$**$*.*   # ~
*.*****************.*   # 여기까지 건물 (건물테두리 . 은 통로)
*...................*   # 건물 밖 통로
*********************

"""