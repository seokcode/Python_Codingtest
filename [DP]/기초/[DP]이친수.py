"""
# 이 문제의 경우에는 1차원 배열로도 풀 수 있다.
* 0으로 끝나는 경우
    앞에 0과 1 모두 올 수 있다.
    so, = D[i-1]
* 1로 끝나는 경우
    앞에 0만 올 수 있다
    앞에 붙는 0을 세트로 생각해서 i-2자리에 0,1을 붙인다고 생각
    so, = D[i-2]
"""
# 이친수 # B_2193
# D[i][0](i자리 이친수, 마지막 0) = D[i-1][0] + D[i-1][1]
# D[i][1](i자리 이친수, 마지막 1) = D[i-1][0] ## 1은 두 번 연속 못옴
# D[1][0] = 0 ## 이친수는 0으로 시작할 수 없음
# D[1][1] = 1 ## '1'인 경우 한가지 존재

d = [0]*91
n = int(input())
d[1] = 1
d[2] = 1
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])
