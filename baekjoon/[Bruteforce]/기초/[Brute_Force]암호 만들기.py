# 암호 만들기 # B_1759
# 재귀함수
# 1.불가능한 경우: i >= alpha의 크기
# 2.정답을 찾은 경우: password의 길이 == n
# 3.다음 경우 호출: i번째 알파벳 사용 / 사용하지 않음


# 최소 한 개의 모음과 두 개의 자음으로 구성되어있는지 확인
def check(password):
    ja = 0
    mo = 0
    for k in password:
        if k in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


def go(n, alpha, password, i):
    # n: 만들어야 하는 암호의 길이
    # alpha: 사용할 수 있는 알파벳이 담긴 리스트
    # password: 현재까지 만든 암호
    # i: 사용할지 말지 결정해야 하는 알파벳의 인덱스(탐색)
    if len(password) == n:  # 2.정답을 찾은 경우
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return
    # 3. 다음 경우 호출
    # 모든 경우 의 수를 계산하고 정답이라면 2번을 통해 조건 부합 여부 계산
    go(n, alpha, password+alpha[i], i+1)  # 해당 알파벳 사용
    go(n, alpha, password, i+1)  # 해당 알파벳 미사용


# n개로 만들기 고를 수 있는 문자는 m개 주어짐
n, m = map(int, input().split())
a = input().split()  # m개의 문자 입력
a.sort()  # 사전 순 정렬
go(n, a, "", 0)
