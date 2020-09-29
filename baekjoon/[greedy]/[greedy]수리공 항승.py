# 수리공 항승 # B_1449

N, L = map(int, input().split())
where = list(map(int, input().split()))
where.sort()  # 물이 새는 곳 오름차순 정렬
s = 0
temp = 0
result = 0
for i in range(N-1):  # 물이 새는 곳의 수보다 -1 하여 탐색(불필요한 탐색 방지)
    temp = where[i+1]-where[i]
    s += temp
    if s + 1 > L:  # >= 이 아닌 이유는 이미 테이핑 한 곳의 불필요한 테이핑 방지
        s = 0
        result += 1

print(result+1)


