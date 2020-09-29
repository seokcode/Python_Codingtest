# 수 이어 쓰기1 # B_1748
# 이 문제의 경우 N이 어마어마하게 크기 때문에 단순한 방법으로는 불가능
"""
N =120 일 때,
1 ~ 9 =>[1자리수 10개] => (9-1+1) * 1
# start = 1 , end = 9
10 ~ 99 => (99-10+1) * 2
100 ~ 120 => (120-100+1) * 3
"""

n = int(input())
ans = 0
start, length = 1, 1

while start <= n:
    end = start*10 - 1
    if end > n:
        end = n
    ans += (end-start+1) * length
    length += 1
    start *= 10

print(ans)