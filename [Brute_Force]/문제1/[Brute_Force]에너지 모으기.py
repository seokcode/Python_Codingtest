# 에너지 모으기 # B_16198
"""
첫번째와 마지막 구슬은 고를 수 없음
3개 구슬이 있다면 처음으로 고를 수 있는 방법은 : 가운데를 고르는 경우 3-2=1가지
4개: 4-2=2가지
10개: 10-2=8가지

그래서 총 8!가지의 방법 존재 = 40,320
"""

def go(w):
    n = len(w)
    if n == 2:
        return 0
    ans = 0
    for i in range(1, n-1):
        energy = w[i-1]*w[i+1]  # 양쪽 구슬의 에너지 모음
        b = w[:i] + w[i+1:]  # i번째 인덱스를 제거
        energy += go(b)  # 다시 선택하러 감

        if ans < energy:
            ans = energy
    return ans


n = int(input())
w = list(map(int, input().split()))
print(go(w))
