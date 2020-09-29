# 최대공약수와 최소공배수 # B_2609
# GCD: 최대 공약수(Greatest Common Divisor
# 방법 1 # 시간 복잡도 O(N)
a, b = map(int, input().split())

# 모든 자연수는 1을 약수로 가짐
g = 1

# N의 약수는 N보다 작을 수 밖에 없다.
# 두 수의 최대 공약수는 두 수 중 작은 수의 공약수보다 클 수 없다.
for i in range(2, min(a, b)):
    if a % i ==0 and b % i == 0:
        g = i

print(g)
# 최소 공배수 = 두 수의 곱(A * B) / GCD(최대 공약수)
print((a*b)//g)

# --------------------------------------------- #
# 방법 2 # 유클리드 호제 # 시간 복잡도 O(log N)
# 유클리드 호제법: GCD(a,b) = GCD(b,r) r== a/b
# a > b 인 상태로 입력이 되지 않아도 재귀 혹은 반복문 첫번째에서 a > b로 맞춰짐
# 세 수: GCD(a,b,c) = GCD(GCD(a,b),c)
# GCD(24, 16) = GCD(16, 8) = GCD(8, 0) = 8법


# 1(재귀)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# 2(반복문)
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

gcd(a, b)
