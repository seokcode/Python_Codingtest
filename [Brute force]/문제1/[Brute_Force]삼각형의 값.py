# 삼각형의 값 # B_4902
# 이해 안되면 실행 순서대로 차근차근 살펴보기
"""
r번 줄에는 2r-1개의 열이 존재
교안 참조

# 정삼각형
        (2,3)
        (3,4)
    (3,3)   (3,5)  # (2,3)에서 좌측은 열만 +1 증가 우측은 열+1 행+2증가
    (4,4)   (4,6)
(4,3)   (4,5)   (4,7) # (3,3) -> (3+1,3), (3,3) -> (3+1,5+2)

# 역삼각형
(3,2)   (3,4)  # (4,4) -> (4-1,4-2), (4,4) ->(4-1,4)
    (3,3)
    (4,4)
"""

def calc(row, left, right, sum):
    if row < 1 or row > n:
        return
    if left < 1 or right > 2*row-1:
        return
    # 이상 범위를 벗어난 경우

    # 현재 누적된 삼각형의 합에 현재 row행의 값을 더해줌
    sum += s[row][right] - s[row][left-1]

    global ans
    if sum > ans:
        ans = sum  # 가장 '큰' 부분 삼각형의 값 저장
    if left % 2 == 0:  # 짝수면 역삼각형 열은 -1 왼쪽 행이 -2
        calc(row-1, left-2, right, sum)
    else:  # 정삼각형 열은 +1 오른쪽 행이 +2
        calc(row+1, left, right+2, sum)


tc = 0
while True:
    tc += 1  # 테스트 케이스 번호
    inputs = list(map(int,input().split()))
    n = inputs[0]  # 0번 인덱스: 삼각형 줄의 수
    if n == 0:  # 0이면 종료
        break
    ans = -100000
    a = [[]]
    s = [[]]
    k = 1

    # **** 기타챕터-구간합 구하기4 **** #
    for i in range(1, n+1):  # 삼각형 줄의 수만큼 반복
        a.append([0]*(2*i))  # 1번 인덱스부터 실제 사용 값
        s.append([0]*(2*i))  # 1번 인덱스부터 실제 사용 값
        for j in range(1, 2*i):  # i번 행에는 2i-1개의 열이 존재
            a[i][j] = inputs[k]
            k += 1

            # i번째 행의 첫번째 열부터 j번째 열까지의 합
            # 삼각형의 i번째 행 제일 우측 열(삼각형)에 i번째 행의 합이 기록됨
            s[i][j] = s[i][j-1] + a[i][j]

    # **** 기타챕터-구간합 구하기4 **** #
    print(a)
    print(s)
    # 모든 삼각형에 대해 반복
    for i in range(1, n+1):  # 행
        for j in range(1, 2*i):  # i번 행에는 2i-1개의 열이 존재
            calc(i,j,j,0)
    print(str(tc)+'. '+str(ans))


