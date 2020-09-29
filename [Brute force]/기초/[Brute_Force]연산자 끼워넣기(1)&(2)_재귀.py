# 연산자 끼워넣기 # B_14888 # & # 연산자 끼워넣기(2) # B_15658
# 연산자 끼워넣기2는 N-1개 '이하'가 아닌 '이상'의 연산자가 있음
# 4^(n-1)의 경우의 수 최대 4^10 이므로 브루트포스 재귀함수 가능
# 일반 연산자 끼워넣기 문제와 같은 소스코드로 해결 가능
# 재귀함수
# 1. 불가능한 경우: 연산자의 갯수가 0보다 작을 떄
# 2. 정답 : index == a-1(연산자는 숫자보다 하나 적음)
# 3. 다음 경우 : 사용함 / 사용안함


def calc(a, index, cur, plus, minus, mul, div):
    # a: 입력으로 주어진 수열
    # index: 현재 계산해야 하는 인덱스
    # cur: index-1번째까지 계산한 결과
    # plus, minus, mul, div: 사용할 수 있는 연산자의 개수함
    if index == len(a):  # 2. 정답
        return cur, cur
    res = []
    if plus > 0:
        res.append(calc(a, index+1, cur+a[index], plus-1, minus, mul, div))
    if minus > 0:
        res.append(calc(a, index+1, cur-a[index], plus, minus-1, mul, div))
    if mul > 0:
        res.append(calc(a, index+1, cur*a[index], plus, minus, mul-1, div))
    if div > 0:
        if cur >= 0:
            res.append(calc(a, index+1, cur//a[index], plus, minus, mul, div-1))
        else:
            res.append(calc(a, index + 1, -(-cur // a[index]), plus, minus, mul, div - 1))

    ans = (max([t[0] for t in res]),min([t[1] for t in res]))

    return ans


n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

# 첫번째 숫자는 계산할 필요 없음 그래서 1부터 시작하고 현재 계산된 숫자:a[0]
ans = calc(a, 1, a[0], plus, minus, mul, div)
print(ans[0])
print(ans[1])