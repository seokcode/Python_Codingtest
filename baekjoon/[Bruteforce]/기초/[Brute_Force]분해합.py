# 분해합 # B_2231
import sys
n = int(input())

for i in range(1, n+1):
    ans = i
    temp = i
    while i != 0:
        ans += i % 10
        i = i//10
    if ans == n:
        print(temp)
        sys.exit()

print(0)

