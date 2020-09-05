# 행렬 # B_1080

N, M = map(int, input().split())
solve = [[0]*M for i in range(N)]  # N*M 행렬 생성
a, b = [], []  # 비교 행렬 a,b


def solution():
    count = 0  # 뒤집기가 실행된 횟수
    for i in range(N-2):  # 3*3 부분 행렬이 상/하로 움직일 경우의 수
        for j in range(M-2):  # 3*3 부분 행렬이 좌/우로 움직일 경우의 수
            if not solve[i][j]:  # 인덱스 값이 False일 경우
                #  3*3 부분 행렬 범위 지정
                for k in range(i, i+3):
                    for q in range(j, j+3):
                        # 뒤집기
                        solve[k][q] = not solve[k][q]
                count += 1
    # 뒤집을 수 있는 경우의 수 만큼 뒤집은 후 검사
    # False가 남아있다면 -1 return
    for i in range(N):
        for j in range(M):
            if not solve[i][j]:
                return -1
    return count  # False가 없다면 count return


# a/b 행렬 입력
for i in range(N):
    a.append(list(input()))
for i in range(N):
    b.append(list(input()))

# a 와 b를 비교하여 일치하지 않은 부분은 False / 일치하는 곳은 True 로 구분
for i in range(N):
    for j in range(M):
        solve[i][j] = a[i][j] == b[i][j]

if N >= 3 and M >= 3:
    print(solution())
else:
    # N/M이 3 미만일 경우 부분 행렬을 적용하지 못하므로 바로 검사
    for i in range(N):
        for j in range(M):
            if not solve[i][j]:
                print(-1)
                exit()
    # 검사를 통과했다면 일치한다는 소리이므로 뒤집기 횟수 0 출력
    print(0)
