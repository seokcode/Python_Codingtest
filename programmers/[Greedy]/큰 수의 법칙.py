# 큰 수의 법칙

# 1
n,m,k = map(int, input().split())
data = list(map(int,input().split()))
data.sort()

first = data[-1]
second = data[-2]

result = 0

while m != 0:
  result += first * k
  result += second
  m -= k+1

print(result)

# 2 - 더 좋은 방법
n,m,k = map(int, input().split())
data = list(map(int,input().split()))

data.sort()
first = data[-1]
second = data[-2]

repeat = (first * k)+second
count = m // (k+1)
result = (repeat * count) + (first * (m - count*(k+1)))

print(result)
