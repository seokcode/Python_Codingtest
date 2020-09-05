# 소수 # B_1978
# N이 소수가 되려면,
# 1) 2보다 크거나 같고 N-1보다 작거나 같은 자연수로 나누어 떨어지면 안된다.
# 시간 복잡도 O(N)

# 2) 2보다 크거나 같고 N/2보다 작거나 같은 자연수로 나누어 떨어지면 안된다.
# 2 * 2/N = N
# 시간 복잡도 O(N/2) = O(N)

# 3) 2보다 크거나 같고 루트N 보다 작거나 같은 자연수로 나누어 떨어지면 안된다.
# ex) 루트24 = 4.xxx 이므로
# 그 기준으로 나누면 24 = 1, 2, 3, 4 |||| 6 ,8, 12, 24 이 나오게 되고
# 4.xxx보다 작거나 같은 자연수로 나누어 떨어지면 소수가 아님을 알 수 있다.
# 시간 복잡도 O(루트N)

n = int(input())

num = list(map(int, input().split()))


def sosu(n):
    i = 2
    if n < 2:
        return False

    while i*i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


cnt = 0
for j in range(len(num)):
    if sosu(num[j]):
        cnt += 1

print(cnt)

