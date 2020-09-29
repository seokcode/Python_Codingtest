# 테트로미노 # 기초편과는 다른 방법 # B_14500
"""
# 테트로미노는 회전하는 경우까지 합쳐서 총 19가지의 도형이 있고
# 하나의 테트로미노당 놓을 수 있는 방법의 개수는 약, O(NM)가지가 있다
# 19*250000 = 4,750,000
# 총 O(19NM)가지로 경우의 수가 많지 않기 때문에 각각의 테트로미노에 대해서 모든 칸에 놓아본다
"""
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n, m = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False]*m for _ in range(n)]


def go(x, y, sum, cnt):  # sum:도형이 차지한 칸들의 숫자의 합/ cnt:도형이 차지한 칸
    if cnt == 4:  # 정사각형 4개를 이어 붙인 것만 테트로미노(4개가 넘어가면 안됨)
        global ans
        if ans < sum:
            ans = sum  # 최댓값 저장
        return
    if x < 0 or x >= n or y < 0 or y >= m:  # 도형이 판을 벗어나는 경우
        return
    if c[x][y]:  # 이번 도형에서 이미 방문했던 칸인 경우
        return
    c[x][y] = True
    for k in range(4):
        go(x+dx[k], y+dy[k], sum+a[x][y], cnt+1)
    c[x][y] = False  # 또 다른 모양의 도형을 위해 초기화


ans = 0
for i in range(n):
    for j in range(m):
        go(i, j, 0, 0)  # 뻐큐모양도형을 제외하고 답 구함
        # 뻐큐모양(보라색)도형은 한 방향으로 이루어지지가 못하기 때문에 예외처리
        if j+2 < m:
            temp = a[i][j] + a[i][j+1] + a[i][j+2]  # -
            if i-1 >= 0:  # ㅗ
                temp2 = temp + a[i-1][j+1]
                if ans < temp2:
                    ans = temp2
            if i+1 < n:  # ㅜ
                temp2 = temp + a[i+1][j+1]
                if ans < temp2:
                    ans = temp2
        if i+2 < n:  # ㅣ
            temp = a[i][j] + a[i+1][j] + a[i+2][j]
            if j+1 < m:  # ㅏ
                temp2 = temp + a[i+1][j+1]
                if ans < temp2:
                    ans = temp2
            if j-1 >= 0:  # ㅓ
                temp2 = temp + a[i+1][j-1]
                if ans < temp2:
                    ans = temp2
print(ans)  # 값 도출
