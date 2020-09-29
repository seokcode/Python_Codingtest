# ATM # B_11399
import sys

people = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))

time.sort()
s = 0

for i in range(people):
    if i != 0:
        time[i] = time[i] + time[i-1]
    s += time[i]

print(s)
