# 부분수열의 합 # B_14225
"""
# S의 부분수열의 갯수는 2^N가지 (N<=20)
# 2^20 = 1,048,576가지
"""
n = int(input())
a = list(map(int, input().split()))
d = [False]*(n*100000+10)


def go(index, sum):
    if index == n:
        d[sum] = True
        return

    go(index+1, sum+a[index])
    go(index+1, sum)


go(0,0)
k = 1
while True:
    if not d[k]:
        print(k)
        break
    k += 1
