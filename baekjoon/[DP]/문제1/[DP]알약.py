# 알약 # B_4811
"""
D[F][H] 약통에 약이 F개 반조각이 H개 있을때, 약을 먹는 모든 방법의 수
1. 한 조각 -> F-1, H+1
2. 반 조각 -> F, H-1

D[F][H] = D[F-1][H+1] + D[F][H-1]
D[F][0] = D[F-1][1]
D[0][H] = 1  # F가 없으면 약 먹는 방법은 하나
"""
limit = 31
d = [[-1]*limit for _ in range(limit)]


def calc(f, h):
    if d[f][h] != -1:
        return d[f][h]
    if f == 0:
        return 1
    if h == 0:
        d[f][h] = calc(f-1, h+1)
        return d[f][h]
    d[f][h] = calc(f-1, h+1) + calc(f, h-1)
    return d[f][h]


while True:
    n = int(input())
    if n == 0:
        break
    print(calc(n, 0))
