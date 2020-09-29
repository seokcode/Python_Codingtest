# GCD 합 # B_9613
num = int(input())
result = 0

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for i in range(num):
    a = list(map(int, input().split()))
    for j in range(1, a[0]):
        for k in range(j+1, a[0]+1):
            result += gcd(a[j], a[k])

    print(result)
    result = 0
