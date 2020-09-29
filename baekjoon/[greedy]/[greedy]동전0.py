# 동전 0 # B_11047
import sys

num, money = map(int, sys.stdin.readline().split())
wallet = []
for i in range(num):
    n = int(sys.stdin.readline())
    wallet.append(n)

count = 0
for i in range(num-1, -1, -1):
    if money // wallet[i] != 0:
        count += money // wallet[i]
        money = money % wallet[i]

print(count)
