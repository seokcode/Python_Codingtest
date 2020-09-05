# 날짜계산 # B_1476
# E:15 S:28 M:19개 이므로 15 * 28 * 19 = 약 8천개 ==> 브루트 포스

E, S, M = map(int, input().split())

year, e, s, m = 0, 0, 0, 0
while True:
    if e == E and s == S and m == M:
        print(year)
        break

    e += 1
    s += 1
    m += 1

    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1

    year += 1
