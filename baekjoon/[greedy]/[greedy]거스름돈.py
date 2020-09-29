# 거스름돈 # B_5585
import sys
input = sys.stdin.readline

money = 1000
change = [500, 100, 50, 10, 5, 1]
to_pay = int(input())

Q = 1000 - to_pay
count = 0
for i in range(len(change)):
    if Q // change[i] != 0:
        count += Q // change[i]
        Q = Q % change[i]

print(count)
