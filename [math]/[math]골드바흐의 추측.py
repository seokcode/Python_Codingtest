# 골드바흐의 추측 # B_6588
# 에라토스테네스의 체
# 시간복잡도 O(NloglogN)

MAX = 1000000
check = [0] * (MAX+1)
check[0] = check[1] = True
prime = []
for i in range(2, MAX+1):
    if not check[i]:
        prime.append(i)
        j = i+i
        while j <= MAX:
            check[j] = True
            j += i

prime = prime[1:]
while True:
    n = int(input())

    if n == 0:
        break
    for p in prime:
        if not check[n-p]:
            print("{0} = {1} + {2}".format(n, p, n-p))
            break
