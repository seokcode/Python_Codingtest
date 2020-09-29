# 크리보드 # B_11058
"""
# D[N] = 버튼을 N번 눌러서 화면에 출력된 A 갯수의 최대값
# 마지막에 1번 버튼을 눌렀을 경우: D[N] = D[N-1] + 1
# * 4번을 사용하려면 3번을 해야하고 3번을 하려면 2번을 해야함
# Ctrl+A, Ctrl+C, Ctrl+V는 꼭 연속으로 눌러야 의미가 있다
# 교안 참고(연습)
# 마지막에 Ctrl+A, Ctrl+C를 누르고 Ctrl+V를 j번 누르면
# D[i] = D[i-(j+2)] * (j+1)
# so, D[i] = max(D[i-1]+1, D[i-(j+2)] * (j+1)) ( 1<= j <= i-3)
"""
n = int(input())
d = [0] * (n+1)

for i in range(1, n+1):
    d[i] = d[i-1]+1
    for j in range(1, i-3+1):
        cur = d[i - (j + 2)] * (j + 1)
        if cur > d[i]:
            d[i] = cur

print(d[n])