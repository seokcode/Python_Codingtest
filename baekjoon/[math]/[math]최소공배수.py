# 최소공배수 # B_1934
num = int(input())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for i in range(num):
    a, b = map(int, input().split())
    GCD = gcd(a,b)
    print((a * b) // GCD)
