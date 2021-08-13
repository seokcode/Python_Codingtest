# 피보나치 수

def solution(n):
    d = [0] * (n + 1)
    d[0], d[1] = 0, 1

    if n < 2: return d[n]

    for i in range(2, n + 1):
        d[i] = d[i - 1] + d[i - 2]

    return (d[n] % 1234567)