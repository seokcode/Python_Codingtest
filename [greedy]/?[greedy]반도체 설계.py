# 반도체 설계 # B_2352
# 테스트 코드 제거 후 제출
import sys
from bisect import bisect

# 답은 맞는데 경로가 이상함
# 도착점과 함께 시작점을 저장해두고 비교한다면 경로또한 완벽하지 않을까?
# 헷갈
input = sys.stdin.readline
n = int(input())
connection = list(map(int, input().split()))
temp = [connection[0]]
print(temp)
for i in range(1, n):
    if connection[i] > temp[-1]:
        print("temp.append:", connection[i])
        temp.append(connection[i])
    else:
        print("위치: ", bisect(temp, connection[i]))
        temp[bisect(temp, connection[i])] = connection[i]
        print(temp)
print(temp)
print(len(temp))