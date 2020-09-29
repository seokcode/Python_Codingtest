# 로또 # B_6603
# 재귀 함수


# 1. 정답: cnt ==6
def go(a, index, lotto):
    # a: 입력으로 주어진 수
    # index: 선택할지 말지 결정해야 하는 인덱스
    # cnt: 현재까지 포함한 수의 개
    if len(lotto) == 6:
        print(' '.join(map(str, lotto)))
        return

    # 2. 불가능: index == a일때 더 이상 선택할 수가 없음
    if index == len(a):
        return
    # 3. index번째를 선택 / 선택하지 않음
    # 아래 순서가 바뀌면 사전순에 어긋나게 됨
    go(a, index+1, lotto+[a[index]])
    go(a, index+1, lotto)


while True:
    # 첫 번째 인덱스와 나머지 인덱스 분리하여 저장
    N, *a = list(map(int, input().split()))
    if N == 0:
        break

    go(a, 0, [])
    print()
