# 1,2,3더하기4 # B_9095
"""
# 1,2,3더하기에서 중복 제거(1+2+3 = 6/ 3+2+1 = 6 같은걸로 취급)
# 다른 중복을 제거하는 조건이나 순서만 다른것은 같은걸로 치는 문제일 경우에도
# 임의의 순서를 정하여 해결
"""
limit = 10000
d = [0] * (limit+1)
d[0] = 1
"""
# 1, 2, 3의 순서로 나오는 것만 세겠다. -> 중복 방지
for i in range(1, limit+1):  # 1
    if i-1 >= 0:
        d[i] += d[i-1]
for i in range(1, limit+1):  # 2
    if i - 2 >= 0:
        d[i] += d[i - 2]
for i in range(1, limit+1):  # 3
    if i - 3 >= 0:
        d[i] += d[i - 3]
"""
nums = [1,2,3]
for i in range(3):
    for j in range(1, limit+1):
        if j - nums[i] >= 0:
            d[j] += d[j-nums[i]]

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])
