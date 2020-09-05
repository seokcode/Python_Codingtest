# 로프 # B_2217
import sys
input = sys.stdin.readline

num = int(input())
weight = []

for i in range(num):
    w = int(input())
    weight.append(w)

weight.sort()
temp = num

for i in range(num):
    weight[i] *= temp
    temp -= 1

print(max(weight))