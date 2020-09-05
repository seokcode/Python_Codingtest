# 저울 # B_2437
import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
w.sort()  # 오름차순 정렬
result = 0

for i in range(n):
    # 추의 무게가 'result+1'의 값보다 크다면 최솟값
    if w[i] > result+1:
        break
    # 그렇지 않다면 result에 추의 무게를 더함
    # 그냥 result로 했을 때에는 모든 최솟값의 경우의 수를 검사 못함
    result += w[i]

print(result+1)