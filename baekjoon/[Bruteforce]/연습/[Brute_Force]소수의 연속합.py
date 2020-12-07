# 소수의 연속합 # B_1644
# 일부만 구하기 + 소수 구하기

# 소수 구하는 중
n = int(input())  # 목표 숫자
check = [False] * (n+1)
primes = []
for i in range(2, n+1):
    if check[i]:
        continue
    j = i*2
    primes.append(i)
    while j <= n:
        check[j] = True  # 소수가 아니면 True
        j += i

left = 0
right = 0
sum = 0 if len(primes) == 0 else primes[0]
ans = 0

while left <= right and right < len(primes):
    if sum <= n:
        if sum == n:
            ans += 1
        right += 1
        if right < len(primes):
            sum += primes[right]
    else:
        sum -= primes[left]
        left += 1

print(ans)

