# 소수 구하기 # B_1929
# 에라토스테네스의 체
# 시간복잡도 O(NloglogN)

MAX = 1000000
check = [0] * (MAX+1)
check[0] = check[1] = True

for i in range(2, MAX+1):
    if not check[i]:
        j = i+i
        while j <= MAX:
            check[j] = True
            j += i

M, N = map(int, input().split())
for i in range(M, N+1):
    if not check[i]:
        print(i)

